import turtle
import time
import os
import sys
import webbrowser
import random
import platform
import getpass
from pathlib import Path, PureWindowsPath
import text_colors as txt
import kshell_exceptions as err

system = platform.system()
user = getpass.getuser()

if system == 'Windows':
    command_options = PureWindowsPath(f'c:/Users/{user}/PycharmProjects/kshell/command_options/')
    invalid_digits = PureWindowsPath(f'c:/Users/{user}/PycharmProjects/kshell/invalid_digits')
else:
    command_options = Path(f'/home/{user}/KShell/command_options')
    invalid_digits = Path(f'/home/{user}/KShell/command_options')

def load():
    print("Loading KShell... ")
    for i in range(0, 100):
        time.sleep(0.05)
        width = int((i + 1) / 4)
        bar = "[" + "#" * width + " " * int((25 - width)) + "]"
        sys.stdout.write("\033[1000D" + bar)
        sys.stdout.flush()
    print("\n\u2192\033[38;2;0;255;0m Loaded KShell!\033[m\n")

def say(commands):
    """This function is called when 'say' is typed; it outputs text using six different options"""
    string = " ".join(commands[2:])
    if commands[1].lower() == "all-caps":
        txt.print_blue(string.upper())
    elif commands[1].lower() == "no-caps":
        txt.print_blue(string.lower())
    elif commands[1].lower() == "cap-first":
        txt.print_blue(string.capitalize())
    elif commands[1].lower() == "title":
        txt.print_blue(string.title())
    elif commands[1].lower() == "swapped-case":
        txt.print_blue(string.swapcase())
    else:
        txt.print_blue(" ".join(commands[1:]))


def say_reverse(commands):
    """This is the little sister of say(), it outputs text backwards"""
    strings = list(commands[1:])
    revstrings = [string[::-1] for string in strings]
    revstrings.reverse()
    output = " ".join(revstrings)
    txt.print_blue(output)


def say_options():
    """This returns the contents of the say-options file, which are the options for the 'say' command"""
    with open(command_options / "say-options.txt", "rt") as options:
        for option in options:
            txt.print_blue(option.rstrip())


def read_file(commands):
    """This is called when 'read' is typed; it reads a file"""
    if commands[1].lower() == "kshell_base.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "kshell_exceptions.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "text_colors.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "functions.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "command_options\\help-command.txt" or \
            commands[1].lower() == "command_options/help-command.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "command_options\\say-options.txt" or \
            commands[1].lower() == "command_options/say-options.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "command_options\\shapes.txt" or \
            commands[1].lower() == "command_options/shapes.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "invalid_digits\\invalid_bin.txt" or \
            commands[1].lower() == "invalid_digits/invalid_bin.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "invalid_digits\\invalid_hex.txt" or \
            commands[1].lower() == "invalid_digits/invalid_hex.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "invalid_digits\\invalid_oct.txt" or \
            commands[1].lower() == "invalid_digits/invalid_oct.txt":
        raise err.ProjectFilesError
    else:
        with open(commands[1], mode="rt", encoding="utf-8") as fin:
            for line in fin:
                txt.print_magenta(line.rstrip())


def write_to_file(commands):
    """This is related to read_file(), it writes to a file"""
    if commands[1].lower() == "kshell_base.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "kshell_exceptions.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "text_colors.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "functions.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "documentation.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "readme.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "command_options\\help-command.txt" or \
            commands[1].lower() == "command_options/help-command.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "command_options\\say-options.txt" or \
            commands[1].lower() == "command_options/say-options.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "command_options\\shapes.txt" or \
            commands[1].lower() == "command_options/shapes.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "invalid_digits\\invalid_bin.txt" or \
            commands[1].lower() == "invalid_digits/invalid_bin.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "invalid_digits\\invalid_hex.txt" or \
            commands[1].lower() == "invalid_digits/invalid_hex.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "invalid_digits\\invalid_oct.txt" or \
            commands[1].lower() == "invalid_digits/invalid_oct.txt":
        raise err.ProjectFilesError
    else:
        with open(commands[1], mode="wt", encoding="utf-8") as fout:
            string = " ".join(commands[2:])
            fout.write(string + "\n")


def append_to_file(commands):
    """This is related to read_file(), it writes to a file"""
    if commands[1].lower() == "kshell_base.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "kshell_exceptions.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "text_colors.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "functions.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "documentation.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "readme.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "command_options\\help-command.txt" or \
            commands[1].lower() == "command_options/help-command.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "command_options\\say-options.txt" or \
            commands[1].lower() == "command_options/say-options.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "command_options\\shapes.txt" or \
            commands[1].lower() == "command_options/shapes.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "invalid_digits\\invalid_bin.txt" or \
            commands[1].lower() == "invalid_digits/invalid_bin.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "invalid_digits\\invalid_hex.txt" or \
            commands[1].lower() == "invalid_digits/invalid_hex.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "invalid_digits\\invalid_oct.txt" or \
            commands[1].lower() == "invalid_digits/invalid_oct.txt":
        raise err.ProjectFilesError
    else:
        with open(commands[1], mode="a", encoding="utf-8") as fout:
            string = " ".join(commands[2:])
            if string == "\\BLANK":
                fout.write("\n")
            else:
                fout.write(string + "\n")

def delete_file(commands):
    """This functions deletes a file"""
    if commands[1].lower() == "kshell_base.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "kshell_exceptions.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "text_colors.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "functions.py":
        raise err.ProjectFilesError
    elif commands[1].lower() == "documentation.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "readme.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "command_options\\help-command.txt" or \
            commands[1].lower() == "command_options/help-command.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "command_options\\say-options.txt" or \
            commands[1].lower() == "command_options/say-options.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "command_options\\shapes.txt" or \
            commands[1].lower() == "command_options/shapes.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "invalid_digits\\invalid_bin.txt" or \
            commands[1].lower() == "invalid_digits/invalid_bin.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "invalid_digits\\invalid_hex.txt" or \
            commands[1].lower() == "invalid_digits/invalid_hex.txt":
        raise err.ProjectFilesError
    elif commands[1].lower() == "invalid_digits\\invalid_oct.txt" or \
            commands[1].lower() == "invalid_digits/invalid_oct.txt":
        raise err.ProjectFilesError
    else:
        file = commands[1]
        os.remove(file)
        print(f"{txt.CYAN}{file}{txt.YELLOW} was deleted!")


def goto_url(commands):
    """This function is called when 'goto-url' is typed; it opens a browser in the specified URL"""
    url_name = str(commands[1])

    if url_name.startswith("https://www."):
        webbrowser.open(url_name)
    elif url_name.startswith("http://www."):
        webbrowser.open(url_name)
    else:
        url_name = "http://www." + url_name
        webbrowser.open(url_name)


def search(commands, format_string):
    """This function searches for a substring in a string; called when 'search' is typed"""
    substring = commands[1]
    string = " ".join(commands[2:])

    if substring in string:
        print(format_string.format(txt.BLUE, txt.MAGENTA,
                                   substring, txt.BLUE, txt.MAGENTA, string,
                                   txt.BLUE, txt.RESET))
    else:
        raise err.InstanceNotFoundError


def help_command():
    """This function returns the contents of help-command.txt; contains all different commands"""
    with open(command_options / "help-command.txt", "rt") as commands:
        for command in commands:
            txt.print_blue(command.rstrip())


def shapes():
    """This function reads the innards of shapes.txt; supported shapes for 'draw'"""
    with open(command_options / "shapes.txt", "rt") as shapes_file:
        for shape in shapes_file:
            txt.print_blue(shape.rstrip())


def draw(commands):
    """This function is called when 'draw' is typed; it draws a specified shape"""
    if commands[1].lower() == "square":
        t = turtle.Turtle()
        draw_rect(t)
    elif commands[1].lower() == "circle":
        t = turtle.Turtle()
        draw_circle(t)
    elif commands[1].lower() == "triangle":
        t = turtle.Turtle()
        draw_triangle(t)
    else:
        raise err.InvalidShapeError


def to_base_10(commands):
    """This function converts an integer (hex, oct, bin) to base 10"""
    integer = commands[1]

    with open(invalid_digits / "invalid_bin.txt", "rt") as inv_bin:
        invalid_bin = [invalid.strip() for invalid in inv_bin]

    with open(invalid_digits / "invalid_oct.txt", "rt") as inv_oct:
        invalid_oct = [invalid.strip() for invalid in inv_oct]

    with open(invalid_digits / "invalid_hex.txt", "rt") as inv_hex:
        invalid_hex = [invalid.strip() for invalid in inv_hex]

    if integer.startswith("0x"):
        integer = integer.replace("0x", "")
        if any(invalid in integer for invalid in invalid_hex):
            raise err.IncorrectIntegerBaseError
        else:
            integer = "0x" + integer
            integer = int(integer, 16)
            txt.print_blue(f"Base 10: {integer}")
    elif integer.startswith("0o"):
        integer = integer.replace("0o", "")
        if any(invalid in integer for invalid in invalid_oct):
            raise err.IncorrectIntegerBaseError
        else:
            integer = "0o" + integer
            integer = int(integer, 8)
            txt.print_blue(f"Base 10: {integer}")
    elif integer.startswith("0b"):
        integer = integer.replace("0b", "")
        if any(invalid in integer for invalid in invalid_bin):
            raise err.IncorrectIntegerBaseError
        else:
            integer = "0b" + integer
            integer = int(integer, 2)
            txt.print_blue(f"Base 10: {integer}")
    else:
        raise err.BaseNotSupportedError


def convert_bases(commands):
    """This converts base 10 integers to other bases (hex, oct, bin)"""
    base = commands[1]
    integer = commands[2]
    base_prefixes = ["0x", "0o", "0b"]
    base_10 = True

    for prefix in base_prefixes:
        if integer.startswith(prefix):
            base_10 = False
        else:
            continue

    if base_10:
        if int(base) == 16:
            integer = int(integer)
            txt.print_blue(f"Base 16 (Hex): {hex(integer)}")
        elif int(base) == 8:
            integer = int(integer)
            txt.print_blue(f"Base 8 (Octal): {oct(integer)}")
        elif int(base) == 2:
            integer = int(integer)
            txt.print_blue(f"Base 2 (Binary): {bin(integer)}")
        else:
            raise err.BaseNotSupportedError
    else:
        raise err.IncorrectIntegerBaseError


def random_number(commands):
    """This function generates a random number from 0 to top_int"""
    if commands[1].startswith("0x"):
        raise err.IncorrectIntegerBaseError
    elif commands[1].startswith("0o"):
        raise err.IncorrectIntegerBaseError
    elif commands[1].startswith("0b"):
        raise err.IncorrectIntegerBaseError
    else:
        top_int = int(commands[1]) + 1
        random_num = random.randint(0, top_int)
        txt.print_blue(f"Your random number is: {random_num}")


def read_documentation():
    """This function reads the documentation.txt file"""
    with open("documentation.txt", "rt") as fin:
        for line in fin:
            txt.print_cyan(line.rstrip())


def draw_rect(t):
    """Makes turtle object draw a square"""
    for i in range(0, 4):
        t.forward(100)
        t.right(90)

    time.sleep(3)
    turtle.clearscreen()
    t.screen.exitonclick()
    turtle.TurtleScreen._RUNNING = True


def draw_circle(t):
    """Makes turtle object draw a circle"""
    t.circle(50)

    time.sleep(3)
    turtle.clearscreen()
    t.screen.exitonclick()
    turtle.TurtleScreen._RUNNING = True


def draw_triangle(t):
    """Makes turtle object draw a triangle"""
    t.forward(100)

    for i in range(0, 2):
        t.left(120)
        t.forward(100)

    time.sleep(3)
    turtle.clearscreen()
    t.screen.exitonclick()
    turtle.TurtleScreen._RUNNING = True

