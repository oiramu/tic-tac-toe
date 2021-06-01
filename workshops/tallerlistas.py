from random import randint
from statistics import mode

def ejercicio1(n):
    lista = []
    for x in range(n):
        lista.append(x+1)
    print('La lista resultante es: ' + str(lista))

def ejercicio2(n):
    lista = []
    suma_total = 0
    for x in range(n):
        lista.append((x+1)*5)
    for x in lista:
        suma_total += x
    promedio = suma_total/n
    print('La suma de los multiplos es: '+str(suma_total)+'\nY su promedio es: '+str(promedio)+'\nLista: '+str(lista))

def ejercicio3(n):
    lista = []
    for x in range(n*2):
        if (x+1) % 2 == 0:
            lista.append(x+1)
    print('La lista resultante es: ' + str(lista))

def ejercicio4(n):
    lista = []
    suma_total = 0
    for x in range(n*2):
        rand = randint(1, 100)
        if rand % 2 == 0:
            lista.append(rand)
    for x in lista:
        suma_total += x
    print('La edad más común fue: '+str(mode(lista))+'\nLa media fue: '+str(int(suma_total/len(lista)))+'\Lista: '+str(lista))

def ejercicio5():
    lista = []
    for x in range(randint(1, 100)):
        rand = randint(1, 256)
        lista.append(rand)
        if rand > 100:
            break
    sumatoria = 0
    for x in lista:
        sumatoria += x
    print('La sumatoria es: '+str(sumatoria)+'\nEl número mayor fue: '+str(lista[len(lista)-1]))

def ejercicio6():
    lista = []
    alpha = 'a'
    for i in range(0, 26):
        lista.append(alpha)
        alpha = chr(ord(alpha)+1) 
    print(str(lista))

def ejercicio7():
    lista = []
    alpha = 'a'
    i = 0
    for i in range(0, 26):
        lista.append(alpha.capitalize())
        alpha = chr(ord(alpha)+1) 
    print(str(lista))

def ejercicio8():
    for i in range (1, 256):
        print(chr(i)+'->'+str(i))

def myFacto(n):
    if n == 1:
        return n
    else:
        return n*myFacto(n-1)

def ejercicio9():
    num = int(input('Ingrese numero para hallar factorial: '))
    mult = ''
    for i in range(1, num+1):
        mult += str(i)+' * '
    print(str(num)+'! Factorial de '+str(num)+' es '+str(myFacto(num))+' porque '+mult[:-3]+' es: '+str(myFacto(num)))

def myFibbo(n):
    n1, n2 = 0, 1
    count = 0
    summ = 0
    while count < n:
        summ += n1
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    return summ

def ejercicio10(n):
    print('La sumatoria de esta secuencia fibonacci es: '+ str(myFibbo(n)))

def ejercicio11():
    sumatoria = 0
    terminos_sucesion = ''
    for i in range(10,50+1):
        terminos_sucesion += "1/"+str(i)+" + "
        sumatoria += 1/i
    print("La sumatoria final fue: "+str(sumatoria)+"\nLa secuencia resultante fue: "+terminos_sucesion[:-3])

def ejercicio12():
    sumatoria = 0
    terminos_sucesion = ''
    for i in range(3,100+1):
        terminos_sucesion += str(i-1)+"/"+str(i)+" + "
        sumatoria += i-1/i
    print("La sumatoria final fue: "+str(sumatoria)+"\nLa secuencia resultante fue: "+terminos_sucesion[:-3])

def ejercicio13(n):
    print("La tabla del "+str(n)+": ")
    for i in range(1, 11):
        print(str(n)+"*"+str(i)+"="+str(i*n))

def ejercicio14():
    for i in range(2,10):
        ejercicio13(i)
        input('Presione para ver la tabla del ' + str(i+1) + '->')

def ejercicio15(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return print(str(n)+ " no es numero primo")
        else:
            return print(str(n)+ " es numero primo")

class alumno: 
    def __init__(self, nombre, apellido, definitiva): 
        self.nombre = nombre 
        self.apellido = apellido
        self.definitiva = definitiva

lista_alumnos = []
lista_alumnos.append(alumno('carlos', 'rodriguez','5.0'))
lista_alumnos.append(alumno('ramona', 'flowers','4.7'))

def ejercicio16():
    print('Los nombres de tus alumnos son: ')
    for obj in lista_alumnos:
        print(obj.nombre)

def ejercicio17():
    print('Los apellidos de tus alumnos son: ')
    i = 0
    while i <= len(lista_alumnos)-1:
        print(str(lista_alumnos[i].apellido))
        i += 1

while True:
    print('\nTaller de listas y estructuras cíclicas\n')
    opcion = int(input('Ingrese una opción de los ejercicios del 1 - 17: '))
    if opcion == 1:
        ejercicio1(int(input('Ingrese cantidad de numeros naturales: ')))
    elif opcion == 2:
        ejercicio2(int(input('Ingrese cantidad de multiplos de 5: ')))
    elif opcion == 3:
        ejercicio3(int(input('Ingrese cantidad de numeros pares: ')))
    elif opcion == 4:
        ejercicio4(int(input('Ingrese cantidad de numeros a generar: ')))
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
        ejercicio10(1000)
    elif opcion == 11:
        ejercicio11()
    elif opcion == 12:
        ejercicio12()
    elif opcion == 13:
        ejercicio13(int(input('Ingrese numero a sacar tabla: ')))
    elif opcion == 14:
        ejercicio14()
    elif opcion == 15:
        ejercicio15(int(input('Ingrese un número: ')))
    elif opcion == 16:
        ejercicio16()
    elif opcion == 17:
        ejercicio17()