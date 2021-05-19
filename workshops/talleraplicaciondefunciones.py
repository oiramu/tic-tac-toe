def funcionPotenciaLoraine(base, exponente):
    resultado = 1
    for x in range(exponente):
        resultado *= base
    return resultado

def pagoPorHoras(horas):
    salario_minimo_mensual = 1000000
    valor_trabajo_por_hora = (salario_minimo_mensual/30)/8
    print('\n(con un valor la hora de $'+str(valor_trabajo_por_hora)+')')
    return valor_trabajo_por_hora * horas

def setTriangulo(simbolo):
    print('     '+simbolo)
    print('    '+simbolo+' '+simbolo)
    print('   '+simbolo+'   '+simbolo)
    print('  '+simbolo+'     '+simbolo)
    print(' '+simbolo+'       '+simbolo)
    print(simbolo+simbolo+simbolo+simbolo+simbolo+simbolo+simbolo+simbolo+simbolo+simbolo+simbolo)

def getPrimo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True

def ejercicio1():
    #es una función incorporada en Python 3. Devuelve el elemento más grande en un iterable o el más grande de dos o más argumentos.
    print("1-max(2,3): " + str(max(2,3)))
    #es una función incorporada en Python 3. Devuelve el elemento más pequeño en un iterable o el más pequeño de dos o más argumentos.
    print("2-min(2,3): " + str(min(2,3)))
    #es una función incorporada en Python 3, que devuelve el cociente y el resto al dividir el número a por el número b. Toma dos números como argumentos a & b. El argumento no puede ser un número complejo.
    print("3-divmod(5,2): " + str(divmod(5,2)))
    #es una función incorporada en Python 3 para convertir un número entero en una cadena hexadecimal en minúscula con el prefijo "0x"
    print("4-hex(16): " + str(hex(16)))
    #es una función incorporada en Python 3. Este método devuelve la longitud (el número de elementos) de un objeto. Toma un argumento x.
    list1 = [123, 'xyz', 'zara'] # lista
    print("5-len(): " + str(len(list1)))
    #es una función incorporada en Python 3, para convertir la cadena que representa un carácter Unicode en un entero que representa el código Unicode del carácter.
    print("6-ord('c'): " + str(ord('c')))
    #es una función incorporada en Python 3, para convertir el número entero que representa el código Unicode en una cadena que representa un carácter correspondiente.
    print("7-chr(49): " + str(chr(49)))
    #para recibir datos del usuario tenemos la función input()
    inp = input('8-input("Ingrese un input: ") Ingrese un input:')
    print(str(inp))
    #Imprime en pantalla el argumento. Devuelve el string argumento.
    print("9-print('Hola'): Hola")
    #Reemplaza una cadena por otra. Devuelve un nuevo string.
    texto = 'Manuel es mi amigo'
    print("texto = 'Manuel es mi amigo'\n10-texto.replace('es', 'era'): " + str(texto.replace('es', 'era')))

def ejercicio2():
    cantidad_de_notas = 3
    notas = []
    promedio = 0
    for x in range(cantidad_de_notas):
        notas.append(float(input('\nIngrese nota n'+str(x+1)+': ')))
    for i in range(cantidad_de_notas):
        print('\nTus notas son: '+str(notas[i]))
        promedio += notas[i]
    print('\nTu promedio es: '+str(promedio/cantidad_de_notas)+'\n')

def ejercicio3():
    base = float(input('\nIngrese base: '))
    exponente = int(input('\nIngrese exponente: '))
    print('\nEl resultado de la potencia es: '+str(funcionPotenciaLoraine(base,exponente))+'\n')

def ejercicio4():
    nombre = str(input('\nNombre: '))
    horas_trabajadas = int(input('\nHoras trabajadas: '))
    print(nombre+' ha trabajado '+str(horas_trabajadas)+' horas, su paga es de: $'+ str(pagoPorHoras(horas_trabajadas))+'\n')

def ejercicio5():
    setTriangulo('*')

def ejercicio6():
    numero = int(input('\nIngrese algún valor: '))
    if getPrimo(numero):
        print(numero, ' Es primo')
    else:
        print(numero, ' No es primo')

if __name__ == "__main__":
    while True:
        print('\nTaller de aplicacion de funciones')
        for x in range(6):
            print(str(x+1)+'- Ejercicio '+str(x+1))
        print('8- Salir')
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
            print('Adios!!!')
            break