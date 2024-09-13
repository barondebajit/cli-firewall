# Python Network Firewall

A simple yet powerful network firewall implemented in Python, capable of filtering incoming and outgoing network traffic based on IP addresses and ports.

## Features

- Real-time packet inspection and filtering
- Rule-based traffic control (IP addresses and ports)
- Actual packet blocking using `netfilterqueue`
- Logging of allowed and blocked packets
- Easy-to-configure rules via the `setconfig` command
- Graceful shutdown and cleanup of iptables rules

## Prerequisites

- Python 3.6+
- Root/Administrator privileges (required for packet interception)
- Make

### System Dependencies

This project was built keeping a **Linux** environment in mind. Using this project in other operating systems may lead to unexpected results.

That said, I plan on releasing a **Windows** version of this project soon.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/barondebajit/cli-firewall.git
   cd cli-firewall
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Simply run the makefile as follows:
   ```bash
   make setup
   ```

## Usage

1. Run the `cli-firewall.py` file using

    ```bash
    python3 cli-firewall.py
    ```

## Logging

The firewall logs all allowed and blocked packets in the `log` directory. It creates a new log file in this directory for every time you run the firewall.

## Caution

This firewall affects your system's network traffic. Be careful when defining rules to avoid locking yourself out or disrupting important services. Always ensure you have an alternative means of accessing your system before applying strict firewall rules.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/barondebajit/cli-firewall/blob/main/LICENSE.md) file for details.

## Disclaimer

This firewall is a educational project and may not be suitable for production environments without further development and testing. Use at your own risk.