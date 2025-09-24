# graficar.py
import pandas as pd
import matplotlib.pyplot as plt

# Definir la ruta del archivo de Excel
ruta_archivo = 'datos/~$ejemplo.xlsx'

# Leer el archivo de Excel y obtener los nombres de las hojas
excel_file = pd.ExcelFile(ruta_archivo)
hojas = excel_file.sheet_names

# Iterar sobre cada hoja y generar la gráfica correspondiente
for hoja in hojas:
    df = pd.read_excel(excel_file, sheet_name=hoja)
    
    # Obtener el nombre de la columna para la serie de datos
    # Asume que la primera columna es la etiqueta y la segunda es el valor
    col_labels = df.columns[0]
    col_values = df.columns[1]
    
    # Generar gráfica de barras
    if 'Barras' in hoja:
        plt.figure(figsize=(10, 6))
        plt.bar(df[col_labels], df[col_values], color='skyblue')
        plt.title(f'Gráfico de Barras - {hoja}')
        plt.xlabel(col_labels)
        plt.ylabel(col_values)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(f'{hoja}_barras.png')
        print(f'Gráfico de barras para {hoja} guardado como {hoja}_barras.png')
    
    # Generar gráfica de pastel
    elif 'Pastel' in hoja:
        plt.figure(figsize=(8, 8))
        plt.pie(df[col_values], labels=df[col_labels], autopct='%1.1f%%', startangle=140)
        plt.title(f'Gráfico de Pastel - {hoja}')
        plt.axis('equal') # Asegura que el círculo sea un círculo
        plt.savefig(f'{hoja}_pastel.png')
        print(f'Gráfico de pastel para {hoja} guardado como {hoja}_pastel.png')

print("Proceso de graficación completado.")