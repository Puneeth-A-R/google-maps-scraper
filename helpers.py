"""File with useful helper functions."""

import sys
import string
from termcolor import colored
from random import choices


def LOG(type, message, *args, **kwargs):
    """Custom Logging function."""

    if type == "ERROR":
        res = ''.join(choices(string.ascii_lowercase + string.digits, k=10))
        print(colored(message, "light_red"))
        #args[0].save_screenshot(f"screenshots2/{res}.png")
        return(colored(f"Screenshot saved at screenshots/{res}.png","light_yellow"))
    elif type == "WARNING":
        return(colored(message, "light_yellow"))
    elif type == "INFO":
        return(colored(message, "light_green"))
    else:
        return(colored("ERROR IN INVOKING ERROR FUNCTION!", "on_light_red"))

def pause_execution():
    """Pause scraper when needed and resume when necessary."""
    ip = input("Scraping paused. Press R to resume or any other key to quit: ")
    if ip.upper() != "R":
        sys.exit(0)
