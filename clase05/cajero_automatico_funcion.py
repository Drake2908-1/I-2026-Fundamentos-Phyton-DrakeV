saldo = 0
def consultar_saldo():
    print("Su saldo actual es: ", saldo)
    return saldo
def depositar():
    global saldo
    monto = float(input("Ingrese el monto a depositar: "))
    if monto <= 0:
        print("Error: el monto a depositar debe ser mayor a 0")
    else:
        saldo += monto
        print("Depósito exitoso. Su nuevo saldo es: ", saldo)
def retirar():
    global saldo
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= 0:
        print("Error: el monto a retirar debe ser mayor a 0")
    elif monto > saldo:
        print("Error: saldo insuficiente")
    else:
        saldo -= monto
        print("Retiro exitoso. Su nuevo saldo es: ", saldo)

while True:
    print("Bienvenido al cajero automatico")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        consultar_saldo()
    elif opcion == 2:
        depositar()
    elif opcion == 3:
        retirar()
    elif opcion == 4:
        print("Gracias por usar el cajero automatico. ")
        break
    else:
        print("Opción no valida. Por favor seleccione una opción del 1 al 4.")
 