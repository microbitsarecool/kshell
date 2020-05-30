BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[m'

# These functions allow simple colored
# text output using the variables above.
def print_black(string):
    """Prints black text"""
    print(f"{BLACK}{string}{RESET}")


def print_red(string):
    """Prints red text"""
    print(f"{RED}{string}{RESET}")


def print_green(string):
    """Prints green text"""
    print(f"{GREEN}{string}{RESET}")


def print_yellow(string):
    """Prints yellow text"""
    print(f"{YELLOW}{string}{RESET}")


def print_blue(string):
    """Prints blue text"""
    print(f"{BLUE}{string}{RESET}")


def print_magenta(string):
    """Prints magenta text"""
    print(f"{MAGENTA}{string}{RESET}")


def print_cyan(string):
    """Prints cyan text"""
    print(f"{CYAN}{string}{RESET}")


def print_white(string):
    """Prints white text"""
    print(f"{WHITE}{string}{RESET}")
