import argparse
import time
import subprocess
import platform
import logging
import os
import shutil
from colorama import init, Fore, Style
import pyfiglet
import signal
import sys

init(autoreset=True)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

FREE_LOCATIONS = ["US", "CA", "DE", "FR", "NL", "UK"]
PAID_LOCATIONS = ["AT", "AU", "BE", "BG", "BR", "CH", "CZ", "DK", "ES", "FI", "HK", "HU", "IE", "IL", "IN", "IT", "JP", "LT", "LV", "MK", "MX", "NO", "NZ", "PL", "PT", "RO", "SE", "SG", "TR"]

def get_windscribe_command():
    if platform.system() == 'Windows':
        return os.environ.get('WINDSCRIBE_PATH', 'C:\\Program Files\\Windscribe\\windscribe-cli')
    elif platform.system() == 'Linux':
        return os.environ.get('WINDSCRIBE_PATH', '/usr/local/bin/windscribe')
    else:
        raise OSError("Unsupported operating system")

def check_command_exists(command):
    if not shutil.which(command):
        raise FileNotFoundError(f"Command not found: {command}")

def change_ip_with_windscribe(location=None):
    windscribe_command = get_windscribe_command()
    check_command_exists(windscribe_command)

    try:
        subprocess.run([windscribe_command, 'disconnect'], check=True)
        if location:
            result = subprocess.run([windscribe_command, 'connect', location], capture_output=True, text=True, check=True)
        else:
            result = subprocess.run([windscribe_command, 'connect'], capture_output=True, text=True, check=True)

        logging.info(Fore.GREEN + result.stdout.strip())
        if result.stderr.strip():
            logging.error(Fore.RED + result.stderr.strip())
    except subprocess.CalledProcessError as e:
        logging.error(Fore.RED + f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
    except Exception as e:
        logging.error(Fore.RED + f"An error occurred: {str(e)}")

def print_title():
    title = pyfiglet.figlet_format("Windscribe", font="small")
    print(Fore.CYAN + title)
    print(Fore.YELLOW + Style.BRIGHT + "Made by Cr0mb")


def select_location():
    print(Fore.YELLOW + "Select the type of location:")
    print(Fore.YELLOW + "1. Free Locations")
    print(Fore.YELLOW + "2. Paid Locations")
    choice = input(Fore.GREEN + "Enter your choice (1 or 2): ").strip()

    if choice == '1':
        locations = FREE_LOCATIONS
    elif choice == '2':
        locations = PAID_LOCATIONS
    else:
        print(Fore.RED + "Invalid choice. Defaulting to Free Locations.")
        locations = FREE_LOCATIONS

    print(Fore.YELLOW + "\nAvailable Locations:")
    for idx, loc in enumerate(locations, start=1):
        print(Fore.YELLOW + f"{idx}. {loc}")

    loc_choice = input(Fore.GREEN + "\nEnter the number of the location you want to connect to: ").strip()
    
    try:
        loc_idx = int(loc_choice) - 1
        if 0 <= loc_idx < len(locations):
            return locations[loc_idx]
        else:
            print(Fore.RED + "Invalid selection. Using default location.")
            return None
    except ValueError:
        print(Fore.RED + "Invalid input. Using default location.")
        return None

def get_change_interval():
    while True:
        try:
            interval_minutes = int(input(Fore.GREEN + "Enter the interval (in minutes) for changing the IP address: ").strip())
            if interval_minutes > 0:
                return interval_minutes * 60
            else:
                print(Fore.RED + "Please enter a positive number.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Windscribe IP Changer CLI")
    parser.add_argument("--location", help="Specify the server location (e.g., US, CA)")
    parser.add_argument("--interval", type=int, help="Specify the change interval in minutes")

    args = parser.parse_args()
    return args

def signal_handler(sig, frame):
    logging.info(Fore.CYAN + "Stopping script and disconnecting from Windscribe...")
    windscribe_command = get_windscribe_command()
    try:
        subprocess.run([windscribe_command, 'disconnect'], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(Fore.RED + f"Error disconnecting from Windscribe: {e}")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print_title()

    args = parse_arguments()
    server_location = args.location
    change_interval_seconds = args.interval * 60 if args.interval else get_change_interval()

    while True:
        try:
            change_ip_with_windscribe(server_location)
            logging.info(Fore.YELLOW + f"IP changed successfully. Next change in {change_interval_seconds // 60} minutes.")
            time.sleep(change_interval_seconds)
        except KeyboardInterrupt:
            logging.info(Fore.CYAN + "Process interrupted. Exiting.")
            break
        except Exception as e:
            logging.error(Fore.RED + f"An error occurred: {str(e)}")
            time.sleep(60)
