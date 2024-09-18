

```python
import subprocess
import sys
import platform
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_banner():
    banner = """
    __  __       _ _   _ _____           _             _         
    |  \/  |     (_) | | |_   _|         | |           | |        
    | \  / | __ _ _| |_| |_| |_ __ _  ___| | _____ _ __| |_ _   _ 
    | |\/| |/ _` | | __| __|  _/ _` |/ __| |/ / _ \ '__| __| | | |
    | |  | | (_| | | |_| |_| || (_| | (__|   <  __/ |  | |_| |_| |
    |_|  |_|\__,_|_|\__|\__\_| \__,_|\___|_|\_\___|_|   \__|\__, |
                                                            __/ |
                                                           |___/ 
                     by kdairatchi
    """
    print(Fore.CYAN + Style.BRIGHT + banner)

def run_naabu(target):
    try:
        command = ['naabu', '-host', target]
        result = subprocess.run(command, capture_output=True, text=True)
        print(Fore.CYAN + "Naabu Output:")
        print(Fore.GREEN + result.stdout)
    except Exception as e:
        print(Fore.RED + f"An error occurred while running naabu: {e}")

def run_nmap(target):
    try:
        command = ['nmap', target]
        result = subprocess.run(command, capture_output=True, text=True)
        print(Fore.CYAN + "Nmap Output:")
        print(Fore.GREEN + result.stdout)
    except Exception as e:
        print(Fore.RED + f"An error occurred while running nmap: {e}")

def run_scapy(target):
    try:
        from scapy.all import IP, ICMP, sr1
        packet = IP(dst=target)/ICMP()
        response = sr1(packet, timeout=2)
        if response:
            print(Fore.GREEN + f"Scapy Output: Host {target} is up.")
        else:
            print(Fore.RED + f"Scapy Output: Host {target} is down or unresponsive.")
    except Exception as e:
        print(Fore.RED + f"An error occurred while running Scapy: {e}")

def choose_scanner():
    print(Fore.MAGENTA + "Choose a scanning tool:")
    print(Fore.CYAN + "[1] Naabu")
    print(Fore.CYAN + "[2] Nmap")
    print(Fore.CYAN + "[3] Scapy")
    choice = input(Fore.YELLOW + "Enter your choice (1, 2, or 3): ")

    if choice not in ['1', '2', '3']:
        print(Fore.RED + "Invalid choice. Please select a valid option.")
        sys.exit(1)

    return choice

def main():
    print_banner()

    target = input(Fore.YELLOW + "Enter the target IP or domain: ")

    scanner_choice = choose_scanner()

    if scanner_choice == '1':
        run_naabu(target)
    elif scanner_choice == '2':
        run_nmap(target)
    elif scanner_choice == '3':
        run_scapy(target)

if __name__ == '__main__':
    main()
```

### Explanation of Changes

1. **Scanner Selection Menu**:
   - The script prompts the user to choose between three different network scanners: `naabu`, `nmap`, and `scapy`.
   - The `choose_scanner()` function presents the menu and takes input from the user to determine which tool to run.

2. **`run_naabu()`**:
   - Executes the `naabu` scan on the target using the command line.
   
3. **`run_nmap()`**:
   - Executes a basic `nmap` scan on the target and prints the output.

4. **`run_scapy()`**:
   - Uses the `scapy` library to send an ICMP request to the target to check if it is up or down.

5. **Error Handling**:
   - All functions are wrapped in `try-except` blocks to handle any errors during the execution of the selected scanner.

### Updated `README.md`

Here’s the updated `README.md` file to reflect the new changes:

---

# Multi-Tool Network Scanner

![Banner](https://via.placeholder.com/728x90.png?text=Multi-Tool+Network+Scanner)  
*A simple, lightweight tool to scan networks using different scanning tools like Naabu, Nmap, and Scapy, with color-enhanced terminal output.*

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [Usage](#usage)
  - [Running the Tool](#running-the-tool)
  - [Example](#example)
- [Error Handling](#error-handling)
  - [Common Issues](#common-issues)
  - [Fixes](#fixes)
- [Contributing](#contributing)
- [License](#license)

## Overview

This tool provides a convenient way to scan network targets using different network scanners, like `naabu`, `nmap`, and `scapy`, with easy-to-read, color-enhanced terminal output.

## Features

- Allows selection of a scanning tool: `naabu`, `nmap`, or `scapy`.
- Displays a banner in color when the tool starts.
- Executes the selected scanner on the target and provides formatted output.
- Error handling to catch issues during execution.

## Installation

### Prerequisites

Before installing this tool, ensure you have the following installed:

- Python 3.x
- `pip` (Python package installer)
- `naabu`, `nmap`, and `scapy`

Install `naabu`:
```bash
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
```

Install `nmap` using your package manager:
```bash
sudo apt-get install nmap  # Debian/Ubuntu
sudo yum install nmap      # CentOS/Fedora
brew install nmap          # macOS
```

Install `scapy` using `pip`:
```bash
pip install scapy
```

### Installation Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/multi-tool-network-scanner.git
    cd multi-tool-network-scanner
    ```

2. **Install Python Dependencies**

    This project requires a few Python libraries, like `colorama`. You can install the required dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure All Scanners are Installed**

    Make sure that `naabu`, `nmap`, and `scapy` are installed.

4. **Run the Tool**

    You are now ready to run the network scanner tool. See the [Usage](#usage) section for details.

## Usage

To scan a target with the tool, use the following command:

```bash
python multi_tool.py
```

You will be prompted to enter a target and choose a scanning tool.

### Running the Tool

1. Enter the target IP or domain.
2. Select one of the following scanning tools:
   - `1` for `Naabu`
   - `2` for `Nmap`
   - `3` for `Scapy`

### Example

```bash
$ python multi_tool.py
```

**Output:**

```plaintext
    __  __       _ _   _ _____           _             _         
    |  \/  |     (_) | | |_   _|         | |           | |        
    | \  / | __ _ _| |_| |_| |_ __ _  ___| | _____ _ __| |_ _   _ 
    | |\/| |/ _` | | __| __|  _/ _` |/ __| |/ / _ \ '__| __| | | |
    | |  | | (_| | | |_| |_| || (_| | (__|   <  __/ |  | |_| |_| |
    |_|  |_|\__,_|_|\__|\__\_| \__,_|\___|_|\_\___|_|   \__|\__, |
                                                            __/ |
                                                           |___/ 
                     by kdairatchi

Enter the target IP or domain: 192.168.1.1

Choose a scanning tool:
[1] Naabu
[2] Nmap
[3] Scapy
Enter your choice (1, 2, or 3): 2
Scanning target: 192.168.1.1

Nmap Output:
Starting Nmap 7.80 ( https://nmap.org ) at 2024-09-17 15:00
Nmap scan report for 192.168.1.1
Host is up (0.00069s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE
80/tcp  open  http
443/tcp open  https
22/tcp  open  ssh
```

## Error Handling

... (same as before, but with mentions of `nmap` and `
