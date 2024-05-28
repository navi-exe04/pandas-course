"""
Arreglo unidimensional que puede contener cualquier tipo de datos (listas para python)
"""
import pandas as pd

# numbers = [1, 2, 3, 4, 5]
# number_series = pd.Series(numbers)
# print(number_series)

materias = ['matematicas', 'fisica', 'ingles', 'musica']
calificaciones = [8, 9 ,7, 10]
serie_materias = pd.Series(index=materias, data=calificaciones) # Se puede definir el index que tendra nuestra serie
# print(serie_materias)
# print(serie_materias.head(2)) # devuele las n primeras filas de la lista
# print(serie_materias.tail(1)) # devuelve las n ultimas filas de la lista

# print(serie_materias.index) # devuelve los index de la serie
# print(serie_materias.values) # devuelve los valores de la serie
# print(serie_materias.dtype) # devuelve el tipo de dato de los valores
# print(serie_materias.size) # regresa el tamaño de la serie
# print(serie_materias.shape) # regresa la forma de la serie
# print(serie_materias.describe()) # regesa un resumen estadistico de la serie
# print(serie_materias.info()) # regresa un resumen de la serie

# print(serie_materias.loc['fisica']) # Regresa los valores por etiqueta
# print(serie_materias.iloc[0]) # Regresa los valores po index
# print(serie_materias.at['matematicas']) # Regesa un solo valor por su etiqueta
# print(serie_materias.iat[1]) # Regresa un solo valor por su index

# print(serie_materias.sum()) # Suma los elementos de la serie
# print(serie_materias.mean()) # Media de los elementos de la serie
# print(serie_materias.median()) # Mediana de los elementos de la serie
# print(serie_materias.mode()) # Moda de los elementos de la serie
# print(serie_materias.min()) # Valor minimo de la serie
# print(serie_materias.max()) # Valor maximo de la serie
# print(serie_materias.std()) # Desviación estandar
# print(serie_materias.var()) # Varianza
# print(serie_materias.count()) # Regresa el numero de elementos nulos
# print(serie_materias.unique()) # Regresa los valores unicos
# print(serie_materias.nunique()) # Regresa el numero de valores unicos
# print(serie_materias.value_counts()) # Regresa la cuenta de frecuencia de los valores
# print(serie_materias.cumsum()) # Suma acumulativa
# print(serie_materias.cumprod()) # Producto acumulativo

serie_materias.replace(to_replace=10, value=100)
print(serie_materias)