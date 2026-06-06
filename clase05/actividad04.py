archivo = open("clase05\lecturaactividad4.txt", "w")
archivo.write("Registro de estudiantes\n")

print("Bienvenido al registro de estudiantes")

Estudiantes = int(input("Cuantos estudiantes desea registrar: "))
Total_de_estudiantes = 0

for i in range (Estudiantes):
    print("\nEstudiante", i + 1)
    nombre = input ("1. Ingrese el nombre del estudiante: ")
    carnet = int(input("2. Ingrese el carnet del estudiante: "))
    nota_final = float(input("3. Ingrese la nota final del estudiante: "))

    if carnet <= 0:
        print("Error: el carnet no puede ser menor a 0")
    elif nota_final < 0 or nota_final > 100:
        print("Error: La nota final debe de estar entre 0 y 100")
    else:
        archivo.write(f"nombre: {nombre}, carnet: {carnet}, nota_final: {nota_final}\n")
        Total_de_estudiantes +=1

archivo.close()   

print("El total de estudiantes registrado es: ", Total_de_estudiantes)

    
