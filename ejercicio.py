#crear un programa que calcule el costo total de una compra en una tienda
#cuatro datos esenciales: el nombre del producto, el precio unitario, 
#la cantidad de productos adquiridos, y el porcentaje de descuento que se aplicará 
# si es que existe alguno
# que el descuento esté dentro del rango aceptable de 0 a 100%.
#
compra=[]

productos=["computador","televisor","lavadora","nevera"]

bienvenida = print("Bienvenido, ¿Qué deseas hacer?")

opcion1= print('1.Ver productos')
opcion2= print ('2.Agregar productos')
opcion3 =print ('3.Ver descuentos')

seleccion_usuario = int(input())

if seleccion_usuario == 1:
    print(productos)
    
elif seleccion_usuario == 2:
    print("que producto deseas agregar")

elif seleccion_usuario ==3:
    print ("descuentos de productos")
    
else :
   print ('ingresa un numero valido')






#nombre_producto = input('Ingresa el nombre del producto: ')

#precio_unitario= float(input(' Cual es el precio: '))

#cantidad_productos = int(input('Cantidad del producto: '))

#porcentaje_descuento = float(input('Descuento del producto: '))

#compra.append(nombre_producto)
#compra.append(precio_unitario)
#compra.append(cantidad_productos)
#compra.append(porcentaje_descuento)

#print(compra)