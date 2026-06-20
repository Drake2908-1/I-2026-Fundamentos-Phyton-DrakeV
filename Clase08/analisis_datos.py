import pandas

#cargar el archivo csv
datos = pandas.read_csv('Clase08/Estudiantes.csv')

#mostrar las primeras filas del dataframe
print(datos.head())

#mostrar solo las columnas "nombre","apellido"
print(datos[["nombre,apellido"]])

#calcular estadísticas descriptivas
print(datos.describe())

#calcular el maximo de la edad
print(datos['edad'].max())

#calcular el minimo de la edad
print(datos['edad'].min())

#filtrar estudiantes con calificacion mayor a 85
estudiantes_alta_nota = datos[datos['nota'] > 85]
print(estudiantes_alta_nota)

#Agrupar por género y calcular la media de las notas
media_por_genero = datos.groupby('sexo')['nota'].mean()
print(media_por_genero)








