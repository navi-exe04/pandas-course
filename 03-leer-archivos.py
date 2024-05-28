import pandas as pd

# Podemos leer un archivo .csv, .xlsx o .json para usarlos como dataframes
# df = pd.read_csv('customers-1000.csv')
# print(df)

# Tambien podemos escribir archivos para usarlos como hojas de calculo
data = {
    'Nombre': ['Ramon', 'Carla', 'Leo', 'Ana'],
    'Edad': [26, 20, 25, 23],
    'Ciudad': ['Chicago', 'Texas', 'New York', None]
}

df = pd.DataFrame(data)
df.to_csv('test.csv', index=None)