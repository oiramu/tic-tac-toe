import datetime

IVA_NACIONAL = 0.2
IVA_INTERNACIONAL = 0.3
FECHA_DE_HOY = datetime.date.today()

def validarCodigo(codigo):
    largo_codigo = len(codigo) 
    tercer_caracter = codigo[2]
    cantidad_de_arrobas = codigo.find("@")
    cantidad_de_iguales = codigo.find("=")
    cantidad_de_positivos = codigo.find('+')
    cantidad_de_ys = codigo.find("&")
    if (largo_codigo == 8 and tercer_caracter == "*" and cantidad_de_arrobas == -1 and codigo[0] == codigo[7] and cantidad_de_positivos == -1 and cantidad_de_iguales == -1 and cantidad_de_ys == -1):
        validar = True
    else:
        validar = False

    return validar

def obtener_color_bicicleta():
    color_id = int(input(("Ingrese color de la bicileta: \n[1] - Roja\n[2] - Negra\n[3] - Roja/Negra\n")))
    if color_id == 1:
        return 'Roja'
    elif color_id == 2: 
        return 'Negra'
    elif color_id == 3:
        return 'Roja/Negra'

def validar_procedencia(marca_id):
    if marca_id == 1 or 3:
        return "Internacional"
    else:
        return "Nacional"  

def calcularIva(precio, marca_id):
    if marca_id == 2:
        return float(precio * IVA_NACIONAL)
    else:
        return float(precio * IVA_INTERNACIONAL)

def calcularComision(total):
    if total >= 200000 and total < 800000:
        return 5
    elif total >= 800000 and total < 1500000:
        return 10
    elif total >= 1500000:
        return 15
    else:
        return 0

def validar_marca(marca_id):
    if marca_id == 1:
        return "Specialized"
    elif marca_id == 2:
        return "Treck"
    elif marca_id == 3:
        return "BMC"

def detalle_venta(id_cliente, nombre_vendedor, nombre_cliente, marca_id, color, size, precio, cantidad):
  precio_neto = precio * cantidad
  precio_iva = calcularIva(precio_neto, marca_id)
  precio_total = precio_neto + precio_iva
  comision = precio_neto * int(calcularComision(precio_neto))
  marca = validar_marca(marca_id)
  procedencia = validar_procedencia(marca_id)

  print("----------------------------------------------------------------------------------------------")
  print("\t\t\t DETALLE DE VENTA PARA EL VENDEDOR")
  print("----------------------------------------------------------------------------------------------")
  print("| COD\t| NOMBRE VENDEDOR\t| MARCA\t| CANTIDAD\t| FECHA VENTA\t| COMISIONES")
  print("|"+codigo+"|"+nombre_vendedor+"\t\t|"+marca+"\t|"+str(cantidad)+"\t|"+str(FECHA_DE_HOY)+"\t|"+str(comision))
  print("\n\n----------------------------------------------------------------------------------------------")
  print("\t\t\t DETALLE DE VENTA PARA EL CLIENTE")
  print("----------------------------------------------------------------------------------------------")
  print("| COD CLIENTE\t| NOMBRE VENDEDOR")
  print("| "+id_cliente+"\t| "+nombre_cliente)
  print("----------------------------------------------------------------------------------------------")
  print("| FECHA VENTA\t| MARCA\t| TIPO\t| VALOR UNIDAD\t| CANTIDAD| TOTAL VENTA\t| IVA\t| TOTAL A PAGAR")
  print("|"+str(FECHA_DE_HOY)+"\t|"+marca+"|"+procedencia+"|"+str(precio)+" |"+str(cantidad)+"\t|"+str(precio_neto)+"\t|"+str(precio_iva)+" |"+str(precio_total))


def obtener_datos_de_venta(es_valido):
  if(es_valido): 
    nombre_vendedor = input("Ingrese el nombre del vendedor: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    id_cliente = input("Ingrese el código del cliente: ")

    print("------------------------------\nInformación de la bicicleta\n------------------------------\n")
    marca_id = int(input(("Ingrese marca de la bicicleta: \n[1] - Specialized\n[2] - Treck\n[3] - BMC\n")))
    color = obtener_color_bicicleta()
    size = (input(("Ingrese tamaño de la bicicleta\n[S] - Small\n[M] - Medium\n[L] - Large\n[XL] - Extra Large\n"))).upper()

    precio = float(input(("Ingrese el precio individual de la bicicleta: ")))
    cantidad = int(input("Ingrese la cantidadidad de bicicletas: "))
    detalle_venta(id_cliente, nombre_vendedor, nombre_cliente, marca_id, color, size, precio, cantidad)

  else:
    print("Codigo inválido! por favor revise la disposición de su código")

codigo = input("Ingrese su código de empleado: ")
validez = validarCodigo(codigo)
obtener_datos_de_venta(validez)