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
