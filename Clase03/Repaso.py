print("Calculadora de IMC")
nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
Edad = int(input("Ingrese su edad: "))
Peso = float(input("Ingrese su peso(KG): "))
Altura = float(input("Ingrese su altura(M): "))
imc = Peso/(Altura**2)

categoria = ""
if imc < 18.5:
    categoria = "bajo peso"
elif imc <= 24.9:
    categoria = "peso normal"
elif imc <= 29.9:
    categoria = "sobrepeso"
elif imc >= 30:
    categoria = "obesidad"
print("Nombre: ", nombre)
print("Edad: ", Edad)
print("Su indice de masa corporal es: ", imc)
print("Categoria: ", categoria)