import logging
from scapy.all import IP, TCP, UDP
from netfilterqueue import NetfilterQueue
from rich import print as rprint
import subprocess
import signal
import sys
import json
import re
import os

def run():
    '''Configuration settings'''
    try:
        with open('config/config.json', 'r') as file:
            config=json.load(file)
    except:
        config={}
    try:
        BANNEDIPS=set(config["BannedIP"])
    except:
        BANNEDIPS=set([])
    try:
        BANNEDPORTS = set(config["BannedPorts"])
    except:
        BANNEDPORTS=set([])
    
    '''Functions'''
    def is_allowed(packet):
        ip_layer=packet.getlayer(IP)
        if ip_layer is None:
            return False

        src_ip=ip_layer.src
        dst_ip=ip_layer.dst

        tcp_layer=packet.getlayer(TCP)
        udp_layer=packet.getlayer(UDP)

        if tcp_layer:
            src_port=tcp_layer.sport
            dst_port=tcp_layer.dport
        elif udp_layer:
            src_port=udp_layer.sport
            dst_port=udp_layer.dport
        else:
            return False

        if (src_ip in BANNEDIPS or dst_ip in BANNEDIPS) and \
        (src_port in BANNEDPORTS or dst_port in BANNEDPORTS):
            return False
        return True

    def process_packet(packet):
        scapy_packet=IP(packet.get_payload())
        if is_allowed(scapy_packet):
            logging.info(f"Allowed: {scapy_packet.summary()}")
            packet.accept()
        else:
            logging.warning(f"Blocked: {scapy_packet.summary()}")
            rprint("[red]Blocked: {}[red]".format(scapy_packet.summary()))
            packet.drop()

    def setup_queue():
        subprocess.run(["iptables", "-F"])
        subprocess.run(["iptables", "-A", "INPUT", "-j", "NFQUEUE", "--queue-num", "1"])
        subprocess.run(["iptables", "-A", "OUTPUT", "-j", "NFQUEUE", "--queue-num", "1"])

    def cleanup_queue():
        subprocess.run(["iptables", "-F"])
        logging.info("Firewall stopped and iptables rules cleared.")

    def signal_handler(sig, frame):
        logging.info("Stopping firewall...")
        cleanup_queue()
        sys.exit(0)

    def runfirewall():
        setup_queue()
        signal.signal(signal.SIGINT, signal_handler)
        nfqueue = NetfilterQueue()
        nfqueue.bind(1, process_packet)
        logging.info("Firewall started.")
        print("Firewall is running. Press Ctrl+C to stop.")
        try:
            nfqueue.run()
        except KeyboardInterrupt:
            pass
        finally:
            nfqueue.unbind()
            cleanup_queue()

    '''Configuring logging'''
    pwd=os.getcwd()
    logs=os.path.join(pwd,"logs")
    if os.path.isdir(logs):
        pass
    else:
        os.makedirs(logs)

    logsfile=[log for log in os.listdir(logs) if re.search("^firewall.",log)]
    lognumber=1
    for i in logsfile:
            lognumber+=1

    logging.basicConfig(filename='logs/firewall{}.log'.format(lognumber), level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
    runfirewall()