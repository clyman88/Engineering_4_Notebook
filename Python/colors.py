from colorama import Style
from colorama import Fore

print(f'This is {Fore.GREEN}color!{Style.RESET_ALL}!')

print("Test" + "\033[1;36m" + "Test")
