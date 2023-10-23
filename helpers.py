"""File with useful helper functions."""

import sys
import string
from termcolor import colored
from random import choices

def pause_execution():
    ip = input("Scraping paused. Press R to resume or any other key to quit")
    if ip.upper() != "R":
        sys.exit(0)

def LOG(type, message, *args, **kwargs):
    """Custom Logging function."""

    if type == "ERROR":
        res = ''.join(choices(string.ascii_lowercase + string.digits, k=10))
        print(colored(message, "light_red"))
        args[0].save_screenshot(f"screenshots2/{res}.png")
        print(
            colored(
                f"Screenshot saved at screenshots/{res}.png",
                "light_yellow"))
    elif type == "WARNING":
        print(colored(message, "light_yellow"))
    elif type == "INFO":
        print(colored(message, "light_green"))
