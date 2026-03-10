import json
import pandas as pd

def leer_datos(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(ruta, lista_datos):
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(lista_datos, f, indent=4, ensure_ascii=False)

def agregar_registro(lista_datos):
    print("\n--- Agregar Nuevo Proyecto ---")
    nuevo_id = max([p['id'] for p in lista_datos], default=0) + 1
    nombre = input("Nombre del proyecto: ")
    horas = int(input("Horas invertidas: "))
    estado = input("Estado (Completado/En proceso): ")
    
    nuevo_p = {"id": nuevo_id, "proyecto": nombre, "horas": horas, "estado": estado}
    lista_datos.append(nuevo_p)
    print("Registro agregado exitosamente.")
    return lista_datos

def generar_reporte_pandas(lista_datos):
    if not lista_datos:
        print("No hay datos para procesar.")
        return

    df = pd.DataFrame(lista_datos)

    print("\n--- REPORTE ESTADÍSTICO (PANDAS) ---")
    print(f"Total de proyectos: {len(df)}")
    print(f"Suma total de horas: {df['horas'].sum()}")
    print(f"Promedio de horas: {df['horas'].mean():.2f}")
    
    resumen_estado = df.groupby('estado')['horas'].count()
    print("\nProyectos por estado:")
    print(resumen_estado)


    df.to_csv('reporte_proyectos.csv', index=False, encoding='utf-8-sig')
    df.to_json('reporte_proyectos_final.json', orient='records', indent=4)
    print("\nArchivos 'reporte_proyectos.csv' y 'reporte_proyectos_final.json' generados.")

def menu():
    ruta_archivo = 'datos.json'
    datos = leer_datos(ruta_archivo)

    while True:
        print("\n=== SISTEMA DE GESTIÓN ADSO ===")
        print("1. Ver registros actuales")
        print("2. Agregar nuevo registro")
        print("3. Generar reporte estadístico y exportar")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            for d in datos: print(d)
        elif opcion == '2':
            datos = agregar_registro(datos)
            guardar_datos(ruta_archivo, datos)
        elif opcion == '3':
            generar_reporte_pandas(datos)
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()