import pandas as pd

df = pd.read_csv('inventario.csv')

print("ANÁLISIS DE INVENTARIO CON PANDAS")

producto_caro = df.loc[df['precio'].idxmax()]
print(f"Producto más costoso: {producto_caro['nombre']} (${producto_caro['precio']})")

producto_mas_stock = df.loc[df['cantidad'].idxmax()]
print(f"Producto con mayor cantidad: {producto_mas_stock['nombre']} ({producto_mas_stock['cantidad']} unidades)")

df['valor_total'] = df['precio'] * df['cantidad']

print("\n--- TABLA ACTUALIZADA ---")
print(df)


df.to_csv('inventario_actualizado.csv', index=False)

print("\n Archivo 'inventario_actualizado.csv' creado")