import pandas as pd
import json

def procesar_datos_sena():
    url = "https://raw.githubusercontent.com/CesarMCuellarCha/archivosCSV/refs/heads/main/SENA.matriculados.json"
    
    try:
        df = pd.read_json(url)
        
        filtro_adso = df[df['PROGRAMA'].str.contains("ANALISIS Y DESARROLLO DE SOFTWARE", na=False, case=False)]
        

        filtro_adso.to_json('ADSO-CTPI.json', orient='records', indent=4, force_ascii=False)
        print("✅ Archivo 'ADSO-CTPI.json' generado con éxito.")
        
        filtro_ficha = filtro_adso[filtro_adso['FICHA'].astype(str) == "3312932"]
        

        condicion_codigo = df['CODIGO_PROGRAMA'].astype(str) == "228118"
        condicion_estado = df['ESTADO_APRENDIZ'].str.strip() == "En transito"
        
        filtro_especifico = df[condicion_codigo & condicion_estado]
        

        cantidad = len(filtro_especifico)
        
        print("\n" + "="*45)
        print(f"RESULTADOS DEL ANÁLISIS")
        print(f"Cantidad de aprendices en tránsito (228118): {cantidad}")
        print("="*45)
        
        if cantidad > 0:

            print(filtro_especifico[['NOMBRE', 'PRIMER_APELLIDO', 'FICHA']])
            
    except Exception as e:
        print(f"Error al procesar los datos: {e}")

if __name__ == "__main__":
    procesar_datos_sena()