import pandas as pd

df = pd.read_json('elecciones.json')

df_mujeres = df[df['Cantidad_Votantes_Mujeres'] > df['Cantidad_Votantes_Hombres']].copy()

df_mujeres['Total_Votantes'] = df_mujeres['Cantidad_Votantes_Hombres'] + df_mujeres['Cantidad_Votantes_Mujeres']

df_mujeres['Porcentaje_Hombres'] = (df_mujeres['Cantidad_Votantes_Hombres'] / df_mujeres['Total_Votantes']).round(2)
df_mujeres['Porcentaje_Mujeres'] = (df_mujeres['Cantidad_Votantes_Mujeres'] / df_mujeres['Total_Votantes']).round(2)

print("Departamentos con mayoría de mujeres ")
print(df_mujeres)


df_mujeres.to_json('mayoría_mujeres_departamento.json', orient='records', indent=4)

print("\n Archivo 'mayoría_mujeres_departamento.json' guardado.")