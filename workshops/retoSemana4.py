def crud(name, lista):
    print('----------------------------')
    print(name.capitalize())
    print('----------------------------')
    print('\t[1] . Ingresar')
    print('\t[2] . Consultar')
    print('\t[3] . Eliminar')
    print('\t[4] . Actualizar')
    print('\t[5] . Listar')
    opcion = int(input('OPCIÓN >> '))

    if opcion == 1:
        lista.append(input('Ingrese '+str(name[:-2])+': '))
    if opcion == 2:
        print(str(lista[int(input('Ingrese id del '+str(name[:-2])+' a consultar: '))]))
    if opcion == 3:
        del lista[int(input('Ingrese id del '+str(name[:-2])+' a eliminar: '))]
    if opcion == 4:
        lista[int(input('Ingrese id del '+str(name[:-2])+' a editar: '))] = input('Ingrese nuevo '+str(name[:-2])+': ')
    elif opcion == 5:
        i = 0
        while i <= len(lista)-1:
            print(' ['+str(i)+'] - '+str(lista[i]))
            i += 1

listas = [[],[],[],[]]
while True:
    print('----------------------------')
    print('ALMACÉN MARKET-CICLE')
    print('PROGRAMA PRINCIPAL')
    print('----------------------------')
    print('\t[1] . Vendedores')
    print('\t[2] . Productos')
    print('\t[3] . Clientes')
    print('\t[4] . Ventas')
    print('\t[5] . SALIR')
    opcion = int(input('OPCIÓN >>> '))

    if opcion == 1:
        crud('vendedores', listas[opcion-1])
    if opcion == 2:
        crud('productos', listas[opcion-1])
    if opcion == 3:
        crud('clientes', listas[opcion-1])
    if opcion == 4:
        crud('ventas', listas[opcion-1])
    elif opcion == 5:
        break