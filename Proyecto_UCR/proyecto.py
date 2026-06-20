
def analizar_contraseña(contraseña):
    puntos = 0
    if len(contraseña) >= 8:
        puntos += 1
        print("✓ La contraseña si tiene al menos 8 caracteres.")
    else:
        print("✗ La contraseña tiene menos de 8 caracteres.")

    tiene_mayuscula = False
    for letra in contraseña:
        if letra.isupper():
            tiene_mayuscula = True

    if tiene_mayuscula:
        puntos += 1
        print("✓ La contraseña contiene letras mayúsculas.")
    else:
        print("X La contraseña no contiene letras mayúsculas.")
    
    tiene_minuscula = False
    for letra in contraseña:
        if letra.islower():
            tiene_minuscula = True

    if tiene_minuscula:
        puntos += 1
        print("✓ La contraseña contiene letras minúsculas.")
    else:
        print("X La contraseña no contiene letras minúsculas.")
    
    tiene_numero = False
    for letra in contraseña:
        if letra.isdigit():
            tiene_numero = True

    if tiene_numero:
        puntos += 1
        print("✓ La contraseña contiene números.")
    else:
        print("✗ La contraseña no contiene números.")

    tiene_caracter_especial = False
    caracteres_especiales = "!@#$%^&*()-_=+[]{};:,.<>?/"
    for letra in contraseña:
        if letra in caracteres_especiales:
            tiene_caracter_especial = True

    if tiene_caracter_especial:
        puntos += 1
        print("✓ La contraseña contiene caracteres especiales.")
    else:
        print("✗ La contraseña no contiene caracteres especiales.") 
        print ("Caracteres permitidos: !@#$%^&*()-_=+[]{};:,.<>?/")
        
    print("\n--- RESUMEN DEL ANÁLISIS ---")
    
    if puntos == 5:
        print("Resultado: ¡Contraseña Muy Segura! 💪")
    elif puntos >= 3:
        print("Resultado: Contraseña Aceptable. ⚠️ Podría mejorar.")
    else:
        print("Resultado: Contraseña Insegura. ❌ ¡Cambiala!")
    return contraseña

    

    

    


while True:
    print("Bienvenido al analizador de contraseñas seguras")
    print("1. Analizar contraseña")
    print("2. Ver contraseñas analizadas")
    print("3. Generar contraseña segura")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        contraseña = input("Ingrese la contraseña a analizar: ")
        analizar_contraseña(contraseña)
    elif opcion == 2:
        print("Contraseñas analizadas:", contraseña)
    elif opcion == 3:
        print("Contraseña segura generada:  ")
    elif opcion == 4:
        print("Gracias por usar el analizador de contraseñas seguras. ")
        break
    else:
        print("Opción no valida. Por favor seleccione una opción del 1 al 3.")