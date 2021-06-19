import os
import colorama
from colorama import Fore, Style, Back
from . import get_args as get_args

colorama.init()

APP_TITLE = ''


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def press_to_continue():
    input(f"\n{Fore.CYAN}{Style.BRIGHT}Presione ENTER para continuar...")
    print(Style.RESET_ALL, end="")


def print_error(msg):
    print(f"\n{Fore.RED}{Style.BRIGHT}Error: {msg}")
    print(Style.RESET_ALL)


def show_banner(subtitle):
    separator = "-"
    separator_len = 25

    print(Fore.GREEN, end="")

    print(separator * separator_len)
    print(APP_TITLE)
    print(Style.BRIGHT + subtitle.upper())
    print(separator * separator_len)

    print(Style.RESET_ALL, end="")


def show_menu(subtitle, options, exit_opt="Salir", use_banner=True):
    last_option = len(options)
    if use_banner:
        clear()
        show_banner(subtitle)

    options_str = ""
    for index, option in enumerate(options):
        print(f"  [{index + 1}]. {option}")
        options_str += str(index + 1)

    print(f"  [{last_option+1}]. {exit_opt}")
    options_str += str(last_option+1)

    option_selected = get_args.get_option(
        options_str, prompt=f"\n{Fore.CYAN}OPCIÓN >>> ")

    print(Style.RESET_ALL, end="")

    if option_selected == str(last_option+1):
        return exit_opt

    return options[
        int(option_selected) - 1
    ]


def show_form(fields, validators=None):
    new_entry = []
    if not validators:
        for field in fields:
            new_entry.append(get_args.get_str(prompt=field + ": "))
        return new_entry

    for field, validator in zip(
        fields, validators
    ):
        value = ""
        if isinstance(
            validator, tuple
        ):
            value = get_args.get_validated(validator, field)
        elif isinstance(validator, int):
            value = get_args.get_int(
                prompt=field + ": ", greater_than=validator)
        else:
            value = get_args.get_str(
                prompt=field + ": "
            )
        new_entry.append(value)
    return new_entry
