from colorama import Fore, Back, Style

SUCCESS = Fore.GREEN + "WEB Back - [SUCCESS]" + Fore.RESET
ERROR   = Fore.RED   + "WEB Back - [ERROR]"   + Fore.RESET
WORKING = Fore.BLUE  + "WEB Back - [WORKING]" + Fore.RESET

def print_log(type, message, method) :
    if (type == "SUCCESS") :
        print('-----------------------------------------')
        print(SUCCESS, message, Fore.BLUE + method + Fore.RESET)
        print('-----------------------------------------')
    elif (type == "ERROR") :
        print('-----------------------------------------')
        print(ERROR, message, Fore.BLUE + method + Fore.RESET)
        print('-----------------------------------------')
    elif (type == "WORKING") :
        print('-----------------------------------------')
        print(WORKING, message, Fore.BLUE + method + Fore.RESET)
        print('-----------------------------------------')

def print_log_data(message) :
    print(message)