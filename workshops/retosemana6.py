import datetime
import os
import matplotlib.pyplot as plt

IVA = 19

# Propilist_ de color de la terminal
class term_color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Método CRUD general para todas las estructuras
# simples del programa, recibe un nombre para manejar
# la nomenclatura de la estructura y recibe la lista
# de esta
def crud(name, lista):
    print('----------------------------')
    print(name.capitalize())
    print('----------------------------')
    print('\t[1] . Ingresar')
    print('\t[2] . Consultar')
    print('\t[3] . Eliminar')
    print('\t[4] . Actualizar')
    print('\t[5] . Listar')

    # Se valida que la opción sea aceptable
    try:
        opcion = int(input('OPCIÓN >>> '))
    except:
        return print(f"{term_color.WARNING}Esta opción no es aceptada!{term_color.ENDC}")

    if opcion == 1:
        lista.append(input(f'{term_color.ENDC}Ingrese ' +
                     str(name[:-2])+': 'f'{term_color.OKGREEN}'))
        print(f'{term_color.OKBLUE}Se ha añadido un nuevo ' +
              str(name[:-2])+f'!{term_color.ENDC}')
    if opcion == 2:
        print(str(lista[int(input(f'{term_color.ENDC}Ingrese id del ' +
              str(name[:-2])+' a consultar: 'f'{term_color.OKCYAN}'))]))
    if opcion == 3:
        del lista[int(input(f'{term_color.ENDC}Ingrese id del ' +
                      str(name[:-2])+' a eliminar: 'f'{term_color.OKCYAN}'))]
        print(f'{term_color.OKBLUE}Se ha eliminado el ' +
              str(name[:-2])+f'!{term_color.ENDC}')
    if opcion == 4:
        lista[int(input(f'{term_color.ENDC}Ingrese id del '+str(name[:-2])+' a editar: 'f'{term_color.OKCYAN}'))
              ] = input(f'{term_color.ENDC}Ingrese nuevo '+str(name[:-2])+': 'f'{term_color.OKGREEN}')
        print(f'{term_color.OKBLUE}Se ha editado el ' +
              str(name[:-2])+f'!{term_color.ENDC}')
    elif opcion == 5:
        i = 0
        while i <= len(lista)-1:
            print(' ['+str(i)+'] - '+str(lista[i]))
            i += 1

# Se maneja un diseño diferente a las ventas dado a la
# complejidad de su estructura no permite compartir la
# misma general que el resto de componentes del software.
# TODO: se podría remover el parametro name, dado que este
# CRUD method es exclusivo para la estructura de las ventas
def crudVentas(name, lista):
    print('----------------------------')
    print(name.capitalize())
    print('----------------------------')
    print('\t[1] . Ingresar')
    print('\t[2] . Consultar')
    print('\t[3] . Eliminar')
    print('\t[4] . Actualizar')
    print('\t[5] . Listar')

    # Se valida que la opción sea aceptable
    try:
        opcion = int(input('OPCIÓN >>> '))
    except:
        return print(f"{term_color.WARNING}Esta opción no es aceptada!{term_color.ENDC}")

    if opcion == 1:
        lista.append(ventaForm())
        print(f'{term_color.OKBLUE}Se ha registrado una nueva venta!{term_color.ENDC}')
    if opcion == 2:
        _id = int(input(
            f'{term_color.ENDC}Ingrese id de la venta a consultar: 'f'{term_color.OKCYAN}'))
        printVenta(lista[_id], _id)
    if opcion == 3:
        del lista[int(input(
            f'{term_color.ENDC}Ingrese id de la venta a eliminar: 'f'{term_color.OKCYAN}'))]
        print(f'{term_color.OKBLUE}Se ha eliminado la venta!{term_color.ENDC}')
    if opcion == 4:
        _id = int(input(
            f'{term_color.ENDC}Ingrese id de la venta a editar: 'f'{term_color.OKCYAN}'))

        lista[_id] = ventaForm()
        print(f'{term_color.OKBLUE}Se ha editado la venta!{term_color.ENDC}')
    elif opcion == 5:
        i = 0
        while i <= len(lista)-1:
            printVenta(lista[i], i)
            i += 1

# Método general para mostrar las tablas de las ventas
# recibe una venta en particular y extrae los datos a
# ser representados, también toma un id para representar
# mejor al usuario cual venta es cual
def printVenta(venta, _id):
    iva_venta = int(venta[3])+((IVA/100)*int(venta[3]))
    total = iva_venta * int(venta[4])
    print(f'{term_color.HEADER}\n--------------------------------------------------------')
    print(f'{term_color.WARNING}CÓDIGO CLIENTE | CÓDIGO VENDEDOR | FECHA VENTA | ID VENTA')
    print(f'{term_color.HEADER}--------------------------------------------------------')
    print(f'{term_color.OKBLUE}', str(venta[0]), '\t|', str(
        venta[1]), '\t|', str(venta[2]), ' |', str(_id))
    print(f'{term_color.HEADER}--------------------------------------------------------')
    print(f'{term_color.WARNING}PRECIO PRODUCTO | CANTIDAD PRODUCTO | IVA | TOTAL')
    print(f'{term_color.HEADER}--------------------------------------------------------')
    print(f'{term_color.OKBLUE}', str(venta[3]), '\t|', str(
        venta[4]), '\t\t|', str(IVA), '% |', str(total))
    print(f'{term_color.HEADER}--------------------------------------------------------\n'f'{term_color.ENDC}')

# Crea un formulario (generico y reutilizable) para la creación
# de una venta, donde se asigna a la lista datos como el
# código del cliente, del vendedor, cantidad de productos y
# añade la propiedad del momento donde se hace la venta
def ventaForm():
    venta = []
    venta.append(
        input(f'{term_color.ENDC}Ingrese código del cliente: 'f'{term_color.OKGREEN}'))
    venta.append(
        input(f'{term_color.ENDC}Ingrese código del vendedor: 'f'{term_color.OKGREEN}'))
    venta.append(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    venta.append(
        input(f'{term_color.ENDC}Precio del producto: 'f'{term_color.OKGREEN}'))
    venta.append(
        input(f'{term_color.ENDC}Cantidad de productos: 'f'{term_color.OKGREEN}'))
    return venta

# Verifica el sistema operativo (windows o unix-like)
# y procede a limpiar la terminal
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def gen_histogram(list_):
    lista_grafico = []
    lista_ids = []

    i = 0
    while i <= len(list_)-1:
        iva_venta = int(list_[i][3])+((IVA/100)*int(list_[i][3]))
        total = iva_venta * int(list_[i][4])
        lista_grafico.append(int(total))
        lista_ids.append("Venta"+str(i))
        i += 1

    plt.bar(lista_ids,lista_grafico,align='center')
    plt.title('Histograma de Ventas')
    plt.xlabel('Ventas')
    plt.ylabel('Precio')
    for i in range(len(lista_grafico)):
        plt.hlines(lista_grafico[i],0,lista_ids[i])

    return plt.show()

def gen_circular(list_):
    lista_grafico = []
    lista_ids = []

    i = 0
    while i <= len(list_)-1:
        iva_venta = int(list_[i][3])+((IVA/100)*int(list_[i][3]))
        total = iva_venta * int(list_[i][4])
        lista_grafico.append(total)
        lista_ids.append("Venta"+str(i))
        i += 1
    plt.pie(lista_grafico, labels=lista_ids)
    plt.axis("equal")
    return plt.show()

def gotoGraficos():
    print('----------------------------')
    print('Graficos')
    print('----------------------------')
    print('\t[1] . Histograma')
    print('\t[2] . Circular')

    # Se valida que la opción sea aceptable
    try:
        opcion = int(input('OPCIÓN >>> '))
    except:
        return print(f"{term_color.WARNING}Esta opción no es aceptada!{term_color.ENDC}")

    if opcion == 1:
        gen_histogram(listas[3])
    elif opcion == 2:
        gen_circular(listas[3])


# Arreglo de arreglos del software (ventas, clientes, etc...)
listas = [[], [], [], []]

# El programa se mantiene en un loop hasta que el usuario decida
# finalizar la ejecución
while True:
    # Se asigna un color para simbolizar la importancia de x dato
    print(f'{term_color.ENDC}----------------------------')
    print('ALMACÉN MARKET-CICLE')
    print('PROGRAMA PRINCIPAL')
    print('----------------------------')
    print('\t[1] . Vendedores')
    print('\t[2] . Productos')
    print('\t[3] . Clientes')
    print('\t[4] . Ventas')
    print('\t[5] . Graficas')
    print('\t[6] . Limpiar Pantalla')
    print('\t[7] . SALIR')

    # Se valida que la opción sea aceptable
    try:
        opcion = int(input('OPCIÓN >>> '))
    except:
        print(f"{term_color.WARNING}Esta opción no es aceptada!{term_color.ENDC}")
        break

    if opcion == 1:
        crud('vendedores', listas[opcion-1])
    if opcion == 2:
        crud('productos', listas[opcion-1])
    if opcion == 3:
        crud('clientes', listas[opcion-1])
    if opcion == 4:
        crudVentas('ventas', listas[opcion-1])
    if opcion == 5:
        gotoGraficos()
    if opcion == 6:
        clear()
    elif opcion == 7:
        print('Adiós!!!!')
        break
