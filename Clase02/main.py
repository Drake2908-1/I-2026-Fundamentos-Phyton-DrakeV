nombre: str = "Drake" 
edad:int = int(input("¿Cuál es tu edad?"))
anno_de_nacimiento:int = 2026 - edad
print(anno_de_nacimiento)
mayor_de_edad:bool = edad >= 18
print(mayor_de_edad)
soy_yo = nombre == "Drake" and edad == 21
print(soy_yo)
no_soy_yo = not(nombre == "Drake" and edad == 21)
print(soy_yo)
quizas_soy_yo = nombre == "Drake" and edad == 21

print(soy_yo)
print(no_soy_yo)
print(quizas_soy_yo)

x = 10
x += 5 
print(x)

