# Desarrolado Por Daniel Eduardo Polo Campo
# ID 201711283751 / CC 1234097443
# Desarrollado por Carlos Rodriguez
# ID 201711285186 / CC 193493462
import random


def imprimirTabla(tabla):
    print('╔══════════════════╗')
    print('╠═══╦═══╦═══╗      ║')
    print('║ 7 ║ 8 ║ 9 ║      ║')
    print('╠═══╬═══╬═══╣      ║')
    print('║ 4 ║ 5 ║ 6 ║ Guia ║')
    print('╠═══╬═══╬═══╣      ║')
    print('║ 1 ║ 2 ║ 3 ║      ║')
    print('╠═══╩═══╩═══╝      ║')
    print('╠══════════════════╣')
    print('╠═══╦═══╦═══╗      ║')
    print('║ '+tabla[7]+' ║ '+tabla[8]+' ║ '+tabla[9]+' ║      ║')
    print('╠═══╬═══╬═══╣      ║')
    print('║ '+tabla[4]+' ║ '+tabla[5]+' ║ '+tabla[6]+' ║      ║')
    print('╠═══╬═══╬═══╣      ║')
    print('║ '+tabla[1]+' ║ '+tabla[2]+' ║ '+tabla[3]+' ║      ║')
    print('╠═══╩═══╩═══╝      ║')
    print('╚══════════════════╝')


def letraJugador(nombreJugador):
    repetir = True
    while repetir:
        print("Juegas con X ó O?")
        letra = input()
        if letra == "x" or letra == "X" or letra == "o" or letra == "O":
            repetir = False
            if letra == "x" or letra == "X":
                return 'X'
            else:
                return 'O'
        else:
            print(nombreJugador + ", " + letra + " no es un caracter valido!")


def primero(nombreJugador):
    if random.randint(0, 1) == 0:
        return 'AL-8999'
    else:
        return nombreJugador


def volverJuego(nombreJugador):
    repetir = True
    while repetir:
        print("¿Quieres volver a jugar Si o No?")
        opcion = input()
        if opcion == "si" or opcion == "Si" or opcion == "SI" or opcion == "s" or opcion == "S":
            return False
            repetir = False
        else:
            if opcion == "no" or opcion == "No" or opcion == "NO" or opcion == "n" or opcion == "N":
                return True
                repetir = False
            else:
                print(nombreJugador + " creo que eso no se puede hacer...")


def colocar(tabla, jugador, movimiento):
    tabla[movimiento] = jugador


def ganar(tabla, Jugador):
    if ((tabla[7] == Jugador and tabla[4] == Jugador and tabla[1] == Jugador) or
            (tabla[8] == Jugador and tabla[5] == Jugador and tabla[2] == Jugador) or
            (tabla[9] == Jugador and tabla[6] == Jugador and tabla[3] == Jugador) or
            (tabla[7] == Jugador and tabla[8] == Jugador and tabla[9] == Jugador) or
            (tabla[4] == Jugador and tabla[5] == Jugador and tabla[6] == Jugador) or
            (tabla[1] == Jugador and tabla[2] == Jugador and tabla[3] == Jugador) or
            (tabla[7] == Jugador and tabla[5] == Jugador and tabla[3] == Jugador) or
            (tabla[9] == Jugador and tabla[5] == Jugador and tabla[1] == Jugador)):
        return True


def copiarTabla(tabla):
    tabla2 = []
    for i in tabla:
        tabla2.append(i)
    return tabla2


def espacioVacio(tabla, movimiento):
    if tabla[movimiento] == ' ':
        return True


def movimientoHumano(tabla,nombreJugador):
    repetir = True
    while repetir:
        movimiento = input()
        if movimiento == '1' or movimiento == '2' or movimiento == '3' or movimiento == '4' or movimiento == '5' or \
                movimiento == '6' or movimiento == '7' or movimiento == '8' or movimiento == '9':
            if espacioVacio(tabla, int(movimiento)):
                repetir = False
                return int(movimiento)
            else:
                print("Ese espacio está ocupado " + nombreJugador)
        else:
            print("Eso ni siquiera es un caracter, aprende a escribir primate")


def movimientoComputador(tabla, computador, humano):
    for i in range(1, 10):
        tablaTemporal = copiarTabla(tabla)
        if espacioVacio(tablaTemporal, i):
            colocar(tablaTemporal, computador, i)
            if ganar(tablaTemporal, computador):
                return i

    for i in range(1, 10):
        tablaTemporal = copiarTabla(tabla)
        if espacioVacio(tablaTemporal, i):
            colocar(tablaTemporal, humano, i)
            if ganar(tablaTemporal, humano):
                return i

    posibleMovimiento = []
    listaMovimiento = [8, 4, 2, 6]
    for i in listaMovimiento:
        if espacioVacio(tabla, i):
            posibleMovimiento.append(i)
        if len(posibleMovimiento) != 0:
            return random.choice(posibleMovimiento)

    if espacioVacio(tabla, 5):
        return 5

    posibleMovimiento = []
    listaMovimiento = [7, 9, 1, 3]
    for i in listaMovimiento:
        if espacioVacio(tabla, i):
            posibleMovimiento.append(i)
        if len(posibleMovimiento) != 0:
            return random.choice(posibleMovimiento)





def tablaLlena(tabla):
    for i in range(1, 10):
        if espacioVacio(tabla, i):
            return False
    return True


nombre = input("Cómo te llamas?")
while True:
    tabla = [' '] * 10
    humano = letraJugador(nombre)
    if humano == 'X':
        computador = 'O'
    else:
        computador = 'X'
    turno = primero(nombre)
    print(turno + ' comienza el turno')
    juegoCorre = True
    while juegoCorre:
        if turno == nombre:
            imprimirTabla(tabla)
            movimiento = movimientoHumano(tabla,nombre)
            colocar(tabla, humano, movimiento)
            if ganar(tabla, humano):
                imprimirTabla(tabla)
                print('Valla, esto si es una novedad, has ganado ' + nombre.lower())
                juegoCorre = False
            else:
                if tablaLlena(tabla):
                    imprimirTabla(tabla)
                    print('Empate!')
                    print('Sorprendente para ser un descendiente del mono')
                    juegoCorre = False
                else:
                    turno = 'AL-8999'
        else:
            movimiento = movimientoComputador(tabla, computador, humano)
            colocar(tabla, computador, movimiento)
            if ganar(tabla, computador):
                imprimirTabla(tabla)
                print('Has Perdido, eres patetico '+ nombre +' >:)')
                juegoCorre = False
            else:
                if tablaLlena(tabla):
                    imprimirTabla(tabla)
                    print('Empate!')
                    print('Honores ' + nombre)
                    juegoCorre = False
                else:
                    turno = nombre
    if volverJuego(nombre):
        print('Esto fue muy divertido ' + nombre + ' nwn')
        exit()
