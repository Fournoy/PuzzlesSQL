

import time

from colorama import Style, Fore

def output_message(message: str) -> None:
    print(f"{Fore.BLUE}{message}{Style.RESET_ALL}")

def warning_message(message: str) -> None:
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")
    
def successful_message(message: str) -> None:
    print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
    
def welcome_message() -> None:
    image =""" 

        .·:''''''''''''''''''''''''''''''''''''''''''''''''''':·.
        : :    ___               _            __    ____  __  : :
        : :   / _ \_   _ _______| | ___  ___ / _\  /___ \/ /  : :
        : :  / /_)/ | | |_  /_  / |/ _ \/ __|\ \  //  / / /   : :
        : : / ___/| |_| |/ / / /| |  __/\__ \_\ \/ \_/ / /___ : :
        : : \/     \__,_/___/___|_|\___||___/\__/\___,_\____/ : :
        '·:...................................................:·'
            """
    print(image)
    time.sleep(2)