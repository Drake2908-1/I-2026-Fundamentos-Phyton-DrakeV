producto = int(input("Bienvenido cuantos productos deseas registrar: "))
nombre = str(input("Ingrese el nombre del producto: "))
precio = float(input("Ingrese el precio del producto: ")) 
cantidad = int(input("Ingrese la cantidad de producto: ")) 
valor_total = nombre and (precio * cantidad)

if producto <= 0:
    print("Ingrese una cantidad de productos correcta por favor: ")
if precio <= 0:
    print("Ingrese un precio correcto por favor: ") 
if cantidad <= 0:
    print("Ingrese una cantidad correcta por favor: ")









