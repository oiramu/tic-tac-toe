import datetime
import math

def ejercicio1():
    nombre = str(input('\nIngrese nombre: '))
    apellido = str(input('Ingrese apellido: '))

    print('\n'+apellido + ' ' + nombre+'\n')

def ejercicio2():
    fecha_de_nacimiento = int(input('\nIngrese año de nacimiento: '))
    año_actual = int(datetime.datetime.now().year)
    print('\nTu edad actual es: '+str(año_actual-fecha_de_nacimiento)+'\n')

def ejercicio3():
    numero_1 = int(input('\nIngrese valor del primer número: '))
    numero_2 = int(input('\nIngrese valor del segundo número: '))
    print('\nLa sumatoría es: '+str(numero_1+numero_2)+'\nLa diferencia es: '+str(numero_1-numero_2)+'\nEl producto es: '+str(numero_1*numero_2)+'\nEl cociente es: '+str(numero_1/numero_2)+'\nEl residuo es: '+str(numero_1%numero_2)+'\n')

def ejercicio4():
    primer_parcial = float(input('\nIngrese nota primer parcial: '))
    segundo_parcial = float(input('\nIngrese nota segundo parcial: '))
    tercer_parcial = float(input('\nIngrese nota tercer parcial: '))

    notas_talleres = [0,0,0]
    for x in range(3):
        notas_talleres[x] = float(input('\nIngrese nota del taller '+str(x+1)+': '))

    nota_definitiva = primer_parcial * .25 + segundo_parcial * .25 + tercer_parcial * .20
    for x in range(3):
        nota_definitiva += notas_talleres[x] * .10
    
    print('\nTu nota definitiva es: '+str(nota_definitiva)+'\n')

def ejercicio5():
    x = int(input('\nIngrese valor de x: '))
    y = int(input('\nIngrese valor de y: '))

    temp = x
    x = y
    y = temp

    print('\nEl valor de x es: '+str(x)+' y el valor de y es: '+str(y)+'\n')

def ejercicio6():
    x = int(input('\nIngrese valor de x: '))
    y = int(input('\nIngrese valor de y: '))

    x, y = y, x

    print('\nEl valor de x es: '+str(x)+' y el valor de y es: '+str(y)+'\n')

def ejercicio7():
    a = float(input('\nIngrese valor de a: '))
    b = float(input('\nIngrese valor de b: '))
    c = float(input('\nIngrese valor de c: '))

    x = [0,0]
    x[0] = -b+math.sqrt(math.pow(b,2)-4*a*c)/2*a
    x[1] = -b-math.sqrt(math.pow(b,2)-4*a*c)/2*a

    print('\n El valor de x1 es: '+str(x[0])+' y el valor de x2 es: '+str(x[1])+'\n')

def ejercicio8():
    caracter = str(input('\nIngrese caracter del teclado: '))
    print('\nEl código ASCII de "'+str(caracter)+'" es: '+str(ord(caracter))+'\n')

def ejercicio9():
    codigo_ascii = int(input('\nIngrese código ASCII: '))
    print('\nEl caracter del código ASCII '+str(codigo_ascii)+' es: "'+str(chr(codigo_ascii))+'"\n')

if __name__ == "__main__":
    while True:
        print('Taller entradas procesos y salidas')
        for x in range(9):
            print(str(x+1)+'- Ejercicio '+str(x+1))
        print('10- Salir')
        opcion = int(input('Introduzca indice del ejercicio a revisar: '))

        if opcion == 1:
            ejercicio1()

        elif opcion == 2:
            ejercicio2()

        elif opcion == 3:
            ejercicio3()
        
        elif opcion == 4:
            ejercicio4()

        elif opcion == 5:
            ejercicio5()

        elif opcion == 6:
            ejercicio6()

        elif opcion == 7:
            ejercicio7()

        elif opcion == 8:
            ejercicio8()

        elif opcion == 9:
            ejercicio9()

        elif opcion == 10:
            print('Adios!!!')
            break