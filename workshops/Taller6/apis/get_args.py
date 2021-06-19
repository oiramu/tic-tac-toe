from . import ui_api


def get_int(msg="", prompt="Ingrese un número entero: ", greater_than=None):
    if msg:
        print(msg)

    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            ui_api.print_error("Ingrese número entero valido")
            continue
        if isinstance(greater_than, int):
            if value <= greater_than:
                ui_api.print_error(f"Ingrese número mayor a {greater_than}")
                continue
        break

    return value


def get_float(
    msg="", prompt="Ingrese un número flotante: ", greater_than=None
):
    if msg:
        print(msg)

    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            ui_api.print_error("Ingrese número flotante valido")
            continue
        if isinstance(greater_than, float):
            if value <= greater_than:
                ui_api.print_error(f"Ingrese número mayor a {greater_than}")
                continue
        break


def get_char(msg="", prompt="Ingrese caracter: "):
    if msg:
        print(msg)

    while True:
        char = input(prompt)
        if char:
            break
        ui_api.print_error("Ingrese al menos un caracter")

    return char[0]


def get_str(msg="", prompt="Ingrese cadena de caracteres: ", max_chars=0):
    if msg:
        print(msg)

    while True:
        string = input(prompt).rstrip()
        if string:
            if max_chars:
                if len(string) <= max_chars:
                    break
                ui_api.print_error(f"Ingrese máximo {max_chars} caracteres")
                continue
            break
        ui_api.print_error("Ingrese al menos un caracter")
    return string


def get_option(options, msg="", prompt="Ingrese opción: ", color=None):
    while True:
        if color:
            print(color, end="")

        option = get_char(msg, prompt)

        if is_valid_option(option, options):
            break
        ui_api.print_error(f"[{option}] NO es una opción valida")

    if color:
        print(ui_api.colorama.Style.RESET_ALL, end="")
    return option


def get_validated(options, msg):
    prompt = "Ingrese opción"
    options_str = ""
    for index, option in enumerate(options):
        prompt += f", {option} [{index + 1}]"
        options_str += str(index + 1)
    prompt += ": "

    option_selected = get_option(options_str, msg, prompt=prompt)

    return options[int(option_selected) - 1]


def get_yes_or_no(
    options="SN", msg="Continuar?", prompt="Digite Si[S], No[N]: "
):
    answer = get_option(
        options[:2], msg, prompt, ui_api.colorama.Fore.LIGHTYELLOW_EX
    )
    return answer.lower() == options[0].lower()


def is_valid_option(option, options):
    if option.lower() in options.lower():
        return True
    return False
