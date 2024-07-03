#%%
# Importamos las librerias necesarias
import pandas as pd
import numpy as np


#%%
def datos_limpios():
    # Cargamos los datos
    df = pd.read_csv('datos_climaticos.csv', header=None)

    # Reemplazamos los headers por sus nombres
    headers = df.iloc[1]
    df.columns = headers

    # Eliminamos la primera y segunda fila
    df = df.drop(0)
    df = df.drop(1)

    # Reemplazamos los (-) con 0 en las columna PP
    df['PP'].replace('-', 0, inplace=True)

    # Reemplazamos los (-) con nulos
    df.replace('-', np.nan, inplace=True)

    # Eliminamos las columnas no necesarias, esta linea solo mantiene las columnas necesarias
    df = df[['Año', 'Mes', 'Día', 'T', 'SLP', 'H', 'PP']]

    # Convertimos las columnas a valores numéricos y se reemplazan los no numéricos con NaN
    df = df.apply(pd.to_numeric, errors='coerce')

    # Eliminamos los valores nulos
    df = df.dropna()

    # Binarizamos la columna PP
    df['PP'] = df['PP'].apply(lambda x: 1 if x > 0 else 0)

    # Se crea el futuro dataset para la red neuronal
    dataset = df[['Mes', 'T', 'SLP', 'H', 'PP']]

    # Equilibramos la columna PP para no sobreajuastar el modelo
    unos = dataset[dataset['PP'] == 1]
    ceros = dataset[dataset['PP'] == 0]

    # Si hay mas ceros que unos, tomamos la muestra aleatoria de ceros del tamaño de unos
    if len(ceros) > len(unos):
        ceros = ceros.sample(len(unos))
    # Si hay mas unos que ceros, tomamos la muestra aleatoria de unos del tamaño de ceros}
    elif len(unos) > len(ceros):
        unos = unos.sample(len(ceros))

    # Combinamos los unos y los ceros equilibrados de nuevo en un solo DataFrame
    dataset = pd.concat([unos, ceros])

    # Ordenamos el DataFrame por la columna Mes
    dataset = dataset.sort_values('Mes')

    # Comprobamos que haya la misma cantidad de unos y ceros
    print('Cantidad de unos:', len(dataset[dataset['PP'] == 1]))
    print('Cantidad de ceros:', len(dataset[dataset['PP'] == 0]))

    # Guardamos el DataFrame y la limpieza de datos en un archivo CSV
    dataset.to_csv('dataset.csv', index=False, header=True)
    df.to_csv('datos_limpios.csv', index=False, header=True)


#%%
# Llamamos a la función para limpiar los datos
datos_limpios()
