from colorama import Fore, Back, Style

SUCCESS = Fore.GREEN + "WEB - [SUCCESS]" + Fore.RESET
ERROR = Fore.RED + "WEB - [SUCCESS]" + Fore.RESET

def print_log(type, string) :
    if (type == "SUCCESS") :
        print(SUCCESS, string)
    elif (type == "ERROR") :
        print(ERROR, string)