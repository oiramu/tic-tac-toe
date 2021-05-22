import math
#Aplica el prinicipio de arquimedes y se implementa una solución
#al problema planteado teniendo en cuenta la longitud de la cuerda
#la longitud de la puerta y el diametro del chewbaca
def reto_semana2(longitud_cuerda, longitud_puerta, chewbaca):
    #Cantidad de vueltas
    r = chewbaca/2
    longitud_polea = 2*math.pi*r
    longitud_cuerda = longitud_puerta/math.sin(45)
    catidad_de_vueltas = longitud_cuerda/longitud_polea
    print('Cantidad de vueltas: '+str(catidad_de_vueltas))

    #Cantidad de chewbacas
    cantidad_de_chewbacas = catidad_de_vueltas/3#vueltas hasta agotarse el chew
    print('Cantidad de chewbacas necesarios: '+str(cantidad_de_chewbacas))

    #Velocidad
    tiempo = 60 #segundos -> 1 minuto
    velocidad = (longitud_cuerda*100)/tiempo
    print('Velocidad de subida: '+str(velocidad)+'cm/s')

if __name__ == "__main__":
    print('Solución reto semana 2')
    reto_semana2(5.88, 5, 0.30)

