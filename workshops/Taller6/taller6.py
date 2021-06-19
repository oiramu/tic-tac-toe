import numpy
import apis.ui_api as user_interface
import apis.get_args as get_args

user_interface.APP_TITLE = "TALLER 6: ARRAYS"

RANGE = (1, 100)

MENU_OPTIONS = (
    "Mostrar Matriz",
    "Mostrar Estadisticas",
    "Ordenar Ascendente",
    "Ordenar Descendente",
    "Generar Nueva Matriz",
)


def new_array():
    n = get_args.get_int(
        "Se generará una matriz de n x n", "Ingrese el valor de n: ", 1
    )
    return numpy.array(generate_array(n))


def generate_array(n):
    rng = numpy.random.default_rng(12345)
    array = rng.integers(low=RANGE[0], high=RANGE[1], size=n * n)
    return array.reshape(n, n)


def print_array(array, subtitle="Matriz Resultados"):
    user_interface.clear()
    user_interface.show_banner(subtitle)
    rows, columns = array.shape

    tot_columns = array.sum(axis=0)
    tot_rows = array.sum(axis=1)

    for i in range(rows):
        for j in range(columns):
            back = ""
            fore = ""
            if j == i:
                back = user_interface.colorama.Back.GREEN
                fore = user_interface.colorama.Fore.RED
            elif j == (columns - i - 1):
                back = user_interface.colorama.Back.CYAN
                fore = user_interface.colorama.Fore.BLACK
            print(back + fore + str(array[i, j]) +
                  user_interface.Style.RESET_ALL, end="\t")

        print(user_interface.colorama.Fore.RED +
              str(tot_rows[i]) + user_interface.Style.RESET_ALL, end="\n")

    for num in tot_columns:
        print(user_interface.colorama.Fore.RED + str(num) +
              user_interface.Style.RESET_ALL, end="\t")


def show_stats(array):
    user_interface.clear()
    user_interface.show_banner("Estadísticas de Matriz")
    print_stats(array)


def print_stats(array):
    print("\nSumatoría =", array.sum())
    print("Promedio =", "{:.2f}".format(array.mean()))
    print(
        "Valor Máximo =",
        array.max(),
        "en fila {}, columna {}".format(
            *numpy.unravel_index(numpy.argmin(array, axis=None), array.shape)
        ),
    )
    print(
        "Valor Mínimo =",
        array.min(),
        "en fila {}, columna {}".format(
            *numpy.unravel_index(numpy.argmin(array, axis=None), array.shape)
        ),
    )


def sort_array(array, reverse=False):
    sorted_array = numpy.sort(array, axis=None)
    if reverse:
        sorted_array = numpy.flip(sorted_array)
    sorted_array = numpy.reshape(sorted_array, newshape=array.shape)
    print_array(sorted_array, "Matriz Ordenada")


def show_array(array):
    print_array(array)
    print_stats(array)


array = None

while True:
    options = (MENU_OPTIONS[-1:] if array is None else MENU_OPTIONS)
    option = user_interface.show_menu("PRINCIPAL MENU", options)

    if option == "Salir":
        user_interface.clear()
        user_interface.show_banner("\n\nHasta luego!\n")
        break
    if option == "Generar Nueva Matriz":
        array = new_array()
        show_array(array)
    elif option == "Mostrar Matriz":
        show_array(array)
    elif option == "Mostrar Estadisticas":
        show_stats(array)
    elif option == "Ordenar Ascendente":
        sort_array(array)
    elif option == "Ordenar Descendente":
        sort_array(array, reverse=True)

    user_interface.press_to_continue()
