"""
Estructura de datos bidimensional (diccionario) con etiquetas
en filas y columnas, similar a una hoja de calculo o tabla SQL
"""
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Nombre': ['Ramon', 'Carla', 'Leo', 'Ana'],
    'Edad': [26, 20, 25, 23],
    'Ciudad': ['Chicago', 'Texas', 'New York', None]
}

df = pd.DataFrame(data)
# print(df)

# Filtrado
# print(df['Nombre']) # Muestra los valores de una columna
# print(df[["Nombre", "Edad"]]) # Muestra los valores de multiples columnas
# print(df[df['Edad'] > 23]) # Filtrado en base a condicion
# print(df[(df['Edad'] > 23) & (df['Ciudad'] == 'Chicago')]) # Multiples condiciones

# Manipulación de datos
# df['Mes de nacimiento'] = ['Abril', 'Septiembre', 'Abril', 'Junio'] # Agregar nueva columna al dataframe
# print(df)
# df = df.drop('Edad', axis=1) # Elimina una columna del dataframe
# df = df.drop([0]) # Eliminar filas
# df = df.rename(columns={'Nombre':'Nombres'}) # Renombrar columnas del dataframe
# df = df.sort_values(by="Edad") # Ordenar datos
# df = df.reset_index(drop=True) # Resetear index en caso de tener otros

# Manipulación de datos faltantes
# print(df.isnull()) # Regresa True o False si hay datos faltantes
# df = df.dropna() # Elimina filas con datos faltantes
# df = df.fillna(0) # Rellena las filas con datos faltantes

# Agregar una nueva fila al dataframe
# df.loc[len(df)] = ['Pedro', 30, 'Illinois']

# Crear graficas con los datos del dataframe
# df['Edad'].plot() # Grafica sencilla
# df.plot(kind='bar', x="Nombre", y="Edad") # Grafica de barras
# plt.show() # Mostrar graficas

# Fusion de dataframes
df2 = pd.DataFrame({
    'Nombre': ['Ramon', 'Carla', 'Leo', 'Ana'],
    'Saldo': [500, 200, 100, 1000]
})

# fusion = pd.merge(df, df2, on='Nombre')
# print(fusion)

# Unir dataframes
# union = pd.concat([df, df2], axis=0) # vertical
union = pd.concat([df, df2], axis=1) # horizontal
print(union)