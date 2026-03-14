import pandas as pd

url = "https://raw.githubusercontent.com/CesarMCuellarCha/archivosCSV/refs/heads/main/deportistas.json"
df = pd.read_json(url)



try:

    col_genero = 'sexo' if 'sexo' in df.columns else 'genero'
    
    df_mujeres = df[df[col_genero] == 'Femenino'].copy()
    df_mujeres.to_json('deportistas_mujeres.json', orient='records', indent=4)
    print("Archivo 'deportistas_mujeres.json' creado.")

    df_ciclismo = df[
        (df['deporte'] == 'Ciclismo de Ruta') & 
        (df['edad'] >= 28) & 
        (df['edad'] <= 35)
    ].copy()
    df_ciclismo.to_json('deportistas_ciclismo_ruta.json', orient='records', indent=4)
    print("Archivo 'deportistas_ciclismo_ruta.json' creado.")

    filtro_baloncesto = df[(df[col_genero] == 'Femenino') & (df['deporte'] == 'Baloncesto')]
    promedio_baloncesto = filtro_baloncesto['edad'].mean()
    print(f"El promedio de edad en Baloncesto Femenino es: {promedio_baloncesto:.2f} años")

    df_hombres = df[df[col_genero] == 'Masculino']
    deportista_mayor = df_hombres.loc[df_hombres['edad'].idxmax()]

    print("\n Deportista Masculino de Mayor Edad ")
    print(f"Nombre: {deportista_mayor['nombre']} | Edad: {deportista_mayor['edad']}")

    df_altos = df[df['estatura'] > 1.85].copy()
    df_altos.to_json('deportistas_estatura_mayor_1.85.json', orient='records', indent=4)
    print(" Archivo 'deportistas_estatura_mayor_1.85.json' creado.")

except KeyError as e:
    print(f"Error: No se encontró la columna {e}")