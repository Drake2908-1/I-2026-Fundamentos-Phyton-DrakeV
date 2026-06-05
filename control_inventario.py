cantidad_productos = int(input("¿Cuántos productos desea registrar?: "))

while cantidad_productos <= 0:
    print("Debe ingresar una cantidad de productos mayor que 0")
    cantidad_productos = int(input("¿Cuántos productos desea registrar?: "))

total_inventario = 0
producto_mas_costoso = ""
mayor_valor = 0

for i in range(cantidad_productos):
    print("\nProducto", i + 1)
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    while precio <= 0:
        print("El precio debe ser mayor que 0")
        precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    while cantidad <= 0:
        print("La cantidad debe ser mayor que 0")
        cantidad = int(input("Ingrese la cantidad del producto: "))

    valor_total = precio * cantidad

    print("Nombre del producto: ", nombre)
    print("Valor total del producto: ", valor_total)

    total_inventario += valor_total

    if valor_total > mayor_valor:
        mayor_valor = valor_total
        producto_mas_costoso = nombre

print("El valor del inventario total es: ", total_inventario)
print("El producto más costoso es:", producto_mas_costoso)
print("Valor del producto más costoso:", mayor_valor)


