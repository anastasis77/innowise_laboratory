from colorama import init, Fore, Back, Style

init()

# Part 2
print(Fore.RED + "Hello, Innowise!" + Fore.RESET)
print(Fore.GREEN + "Hello, Innowise!" + Fore.RESET)
print(Fore.BLUE + "Hello, Innowise!" + Fore.RESET)

# Part 3
print(Fore.BLUE + Style.BRIGHT + "Hello World in Bright Blue!" + Style.RESET_ALL)
print(Fore.MAGENTA + Back.CYAN + "Hello World with Magneta text and Cyan background!" + Style.RESET_ALL)
print(Back.YELLOW + Fore.BLACK + "Hello World with yellow background and Black text!" + Style.RESET_ALL)