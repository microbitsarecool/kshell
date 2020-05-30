# Total number of code lines (including functions.py): 232

# imports the modules: colorama, datetime, webbrowser, os, random
import os
import datetime
import functions as fn  # grabs functions from functions.py
import text_colors as txt  # grabs coloring functions
from text_colors import RED, GREEN, BLUE, CYAN, RESET  # grabs color variables
import kshell_exceptions as err

# This is the non-formatted version of the search
# command's success string. The curly braces represent
# empty spaces which can be formatted with format()
search_success_string = '''{}An instance of {}"{}"{} was found in
{}"{}"{}!
'''

# is_running is set to False when 'exit' is typed
is_running = True
echo_mode = False
version = "0.41 (In-Dev)"

fn.load()
txt.print_magenta(f"KShell Version {version}")
txt.print_magenta("Echo mode is currently set to false; to turn it on, type 'echo-mode true'.")
txt.print_magenta("To turn echo mode off, type 'echo-mode false'.")
txt.print_cyan("Written in Python 3. Make sure to run with Python 3.6 (preferably 3.7) or higher.")
txt.print_magenta("Please enjoy! Report any bugs (Traceback errors, etc.) to microbitsarecool@gmail.com.")
txt.print_magenta("See the documentation or type 'help' for more information.")
# while is_running is True, it loops
while is_running:
    # This is the prompt at which the user enters commands
    prompt = input(f"{GREEN}KShell: {RESET}")

    if echo_mode:
        if prompt == "echo-mode false" or prompt == "ecm false":
            echo_mode = False
            print("\u2192 \033[38;2;128;0;0;4mEcho mode has been set to false!\033[m")
        elif prompt == "exit" or prompt == "x!":
            txt.print_blue("Bye!")
            is_running = False
        else:
            txt.print_cyan(prompt)
    else:

        # This splits the resulting input string into an list based on
        # whether or not there is a ' ' character separating input
        commands = prompt.split(" ")

        # This loops through each element in the commands list and
        # strips all whitespace off each string element
        for i in range(len(commands)):
            commands[i] = commands[i].strip()

        # if the command is 'say' then try to print message based on
        # the option, but if the string isn't provided, write an error
        # message
        if commands[0].lower() == "say" or commands[0].lower() == "s":
            try:
                if len(commands) >= 2:
                    fn.say(commands)
                else:
                    raise err.FieldNotProvidedError
            except err.FieldNotProvidedError:
                txt.print_red("FieldNotProvidedError: Cannot execute: not enough arguments!")
        # if the command is 'say-reverse' then try to print reverse message
        # but if a string isn't provided, print an error message.
        elif commands[0].lower() == "say-reverse" or commands[0].lower() == "srev":
            try:
                if len(commands) >= 2:
                    fn.say_reverse(commands)
                else:
                    raise err.FieldNotProvidedError
            except err.FieldNotProvidedError:
                txt.print_red("FieldNotProvidedError: Cannot execute: not enough arguments!")
        # if the command is 'search', try to get a substring and
        # a string. If the substring is inside the string, print a
        # formatted version of the search_success_string, notifying
        # the user that it was successful. If it's not, notify the
        # user that nothing was found. If some of the fields aren't
        # provided, print an error message.
        elif commands[0].lower() == "search" or commands[0].lower() == "gss":
            try:
                if len(commands) >= 3:
                    fn.search(commands, search_success_string)
                else:
                    raise err.FieldNotProvidedError
            except err.FieldNotProvidedError:
                txt.print_red("FieldNotProvidedError: Cannot execute: not enough arguments!")
            except err.InstanceNotFoundError:
                txt.print_red("InstanceNotFoundError: No instances were found!")
        # if the command is 'say-options', print each option in the
        # say_options list.
        elif commands[0].lower() == "say-options" or commands[0].lower() == "sopt":
            fn.say_options()
        # if the command is 'time' display current time using
        # datetime.datetime.now()
        elif commands[0].lower() == "time" or commands[0].lower() == "tm":
            txt.print_blue(str(datetime.datetime.now()))
        # if the command is 'read' then try to open the file and read each
        # line. If no filename is provided, an error message is printed out,
        # and if the file is not found, print an error message. Finally, if
        # permission is denied, print an error message.
        elif commands[0].lower() == "read" or commands[0].lower() == "rd":
            try:
                if len(commands) >= 2:
                    fn.read_file(commands)
                else:
                    raise err.FieldNotProvidedError
            except err.FieldNotProvidedError:
                txt.print_red("FieldNotProvidedError: Cannot execute: not enough arguments!")
            except err.ProjectFilesError:
                txt.print_red("ProjectFilesError: you cannot read or modify project files!!")
            except FileNotFoundError:
                txt.print_red("File does not exist!")
            except PermissionError:
                txt.print_red("You do not have permission to read this file. :/")
        # if the command is 'write' then try to write to the provided filename
        # and if the filename was not provided or the string was not provided,
        # write an error message. If permission is denied, also write an error.
        elif commands[0].lower() == "write" or commands[0].lower() == "wrt":
            try:
                if len(commands) >= 3:
                    fn.write_to_file(commands)
                else:
                    raise err.FieldNotProvidedError
            except err.FieldNotProvidedError:
                txt.print_red("FieldNotProvidedError: Cannot execute: not enough arguments!")
            except err.ProjectFilesError:
                txt.print_red("ProjectFilesError: you cannot read or modify project files!!")
            except PermissionError:
                txt.print_red("You do not have permission to write to this file. :/")
        elif commands[0].lower() == "append" or commands[0].lower() == "apd":
            try:
                if len(commands) >= 3:
                    fn.append_to_file(commands)
                else:
                    raise err.FieldNotProvidedError
            except err.FieldNotProvidedError:
                txt.print_red("FieldNotProvidedError: Cannot execute: not enough arguments!")
            except err.ProjectFilesError:
                txt.print_red("ProjectFilesError: you cannot read or modify project files!!")
            except PermissionError:
                txt.print_red("You do not have permission to write to this file. :/")
        # if the command is 'delete', try to remove the file
        # and notify when deleted. If no filename was provided,
        # then write an error and if the file was not found,
        # write an error message.
        elif commands[0].lower() == "delete" or commands[0].lower() == "del":
            try:
                if len(commands) >= 2:
                    fn.delete_file(commands)
                else:
                    raise err.FieldNotProvidedError
            except err.FieldNotProvidedError:
                txt.print_red("FieldNotProvidedError: Cannot execute: not enough arguments!")
            except err.ProjectFilesError:
                txt.print_red("ProjectFilesError: you cannot read or modify project files!!")
            except FileNotFoundError:
                print(f"{CYAN}{commands[1]}{RED} does not exist!")
        # if the command is 'goto-url', see if the url_name
        # starts with http://www. or https://www. and if it
        # doesn't, concatenate 'http://www.' to the beginning
        # of the url_name. Then, open the url. If no url
        # is provided, write an error message.
        elif commands[0].lower() == "goto-url" or commands[0].lower() == "gtu":
            try:
                if len(commands) >= 2:
                    fn.goto_url(commands)
                else:
                    raise err.FieldNotProvidedError
            except err.FieldNotProvidedError:
                txt.print_red("FieldNotProvidedError: Cannot execute: not enough arguments!")
        # if the user presses enter without typing anything, ignore it.
        elif commands[0].lower() == "":
            pass
        elif commands[0].lower() == "//":
            pass
        elif commands[0].lower() == "comment:":
            pass
        # if the command is 'help' then loop through available commands
        # and print each one.
        elif commands[0].lower() == "help" or commands[0].lower() == "?":
            fn.help_command()
        # if the command is 'exit' print a goodbye message and set
        # is_running to False, ending the while loop and ending the prog.
        elif commands[0].lower() == "exit" or commands[0].lower() == "x!":
            txt.print_blue("Bye!")
            is_running = False
        # if the command is 'draw' try to figure out which shape was
        # provided and if it's an invalid shape, print error msg,
        # if no shape is provided, also print an error message,
        # otherwise draw the shape.
        elif commands[0].lower() == "draw" or commands[0].lower() == "dr":
            try:
                if len(commands) >= 2:
                    fn.draw(commands)
                else:
                    raise err.FieldNotProvidedError
            except err.FieldNotProvidedError:
                txt.print_red("FieldNotProvidedError: Cannot execute: not enough arguments!")
            except err.InvalidShapeError:
                txt.print_red("InvalidShapeError: Invalid shape!")
        # if the command is 'to-base-10', try to figure out which int
        # was provided using startswith and converting it based upon this.
        # If the base does not match, provide an error message. If the
        # user doesn't provide some fields, write an error, and if the
        # user writes the wrong integer, write an error as well.
        elif commands[0].lower() == "to-base-10" or commands[0].lower() == "tbt":
            try:
                if len(commands) >= 2:
                    fn.to_base_10(commands)
                else:
                    raise err.FieldNotProvidedError
            except err.FieldNotProvidedError:
                txt.print_red("FieldNotProvidedError: Cannot execute: not enough arguments!")
            except err.BaseNotSupportedError:
                txt.print_red("BaseNotSupportedError: Base not supported!")
            except err.IncorrectIntegerBaseError:
                txt.print_red("IncorrectIntegerBaseError: Hex uses digits 0-9 and A-F, Octal uses 0-7, Binary uses 0 "
                              "and 1")
        # if the command is 'convert-bases', then try to figure out
        # which base the user provided and convert it based upon that.
        # If the base does not match, provide an error message.
        # If some of the fields aren't provided, write an error,
        # and if the user doesn't provide base-10, write an error.
        elif commands[0].lower() == "convert-bases" or commands[0].lower() == "cvb":
            try:
                if len(commands) >= 3:
                    fn.convert_bases(commands)
                else:
                    raise err.FieldNotProvidedError
            except err.FieldNotProvidedError:
                txt.print_red("FieldNotProvidedError: Cannot execute: not enough arguments!")
            except err.BaseNotSupportedError:
                txt.print_red("BaseNotSupportedError: Base not supported!")
            except err.IncorrectIntegerBaseError:
                txt.print_red("IncorrectIntegerBaseError: Integer only accepts base-10 numbers!")
        # if the command is 'random-number', try to convert top-int
        # to an integer and add 1 to it. Then generate a random number
        # from 0 to top_int and print it out. If the integer wasn't
        # provided, write an error message and if the integer isn't
        # base-10, write an error.
        elif commands[0].lower() == "random-number" or commands[0].lower() == "rnd":
            try:
                if len(commands) >= 2:
                    fn.random_number(commands)
                else:
                    raise err.FieldNotProvidedError
            except err.FieldNotProvidedError:
                txt.print_red("FieldNotProvidedError: Cannot execute: not enough arguments!")
            except err.IncorrectIntegerBaseError:
                txt.print_red("IncorrectIntegerBaseError: Integer only accepts base-10 numbers!")
        elif commands[0].lower() == "echo-mode" or commands[0].lower() == "ecm":
            try:
                if len(commands) >= 2:
                    if commands[1].lower() == "true":
                        echo_mode = True
                        print("\u2192 \033[38;2;50;205;50;4mEcho mode has been set to true!\033[m")
                    elif commands[1].lower() == "false":
                        echo_mode = False
                        print("\u2192 \033[38;2;128;0;0;4mEcho mode has been set to false!\033[m")
                    else:
                        raise err.UnknownTypeError
                else:
                    raise err.FieldNotProvidedError
            except err.FieldNotProvidedError:
                txt.print_red("FieldNotProvidedError: Cannot execute: not enough arguments!")
            except err.UnknownTypeError:
                txt.print_red("UnknownTypeError: boolean did not match 'true' or 'false'!")
        elif commands[0].lower() == "documentation" or commands[0].lower() == "doc":
            fn.read_documentation()
        # if the command is 'shapes' loop through the shapes list
        # and print each one out.
        elif commands[0].lower() == "shapes" or commands[0].lower() == "shp":
            fn.shapes()
        # if the command does not match any of the above if tests, print
        # an error message.
        else:
            try:
                raise err.CommandDoesNotExistError
            except err.CommandDoesNotExistError:
                print(f"{RED}CommandDoesNotExistError: {BLUE}{commands[0]}{RED} could not be executed.")

