import json

def analizar_ventas(archivo_in, archivo_out):
    try:
        with open(archivo_in, 'r', encoding='utf-8') as f:
            datos_ventas = json.load(f)

        totales_vendedor = {}
        conteo_meses = {}
        suma_ventas_total = 0

        for registro in datos_ventas:
            vend = registro['vendedor']
            monto = registro['ventas']
            

            totales_vendedor[vend] = totales_vendedor.get(vend, 0) + monto
            

            suma_ventas_total += monto
            
        promedio = suma_ventas_total / len(datos_ventas) if datos_ventas else 0


        mejor_vendedor = max(totales_vendedor, key=totales_vendedor.get)

        ranking = sorted(totales_vendedor.items(), key=lambda item: item[1], reverse=True)
        ranking_final = [{"vendedor": v, "total": t} for v, t in ranking]

        with open(archivo_out, 'w', encoding='utf-8') as f_out:
            json.dump(ranking_final, f_out, indent=4, ensure_ascii=False)
            
        print("--- REPORTE DE VENTAS ---")
        for v, t in totales_vendedor.items():
            print(f"Vendedor: {v:<10} | Total: ${t:>8.2f}")
        
        print("-" * 30)
        print(f"Promedio de ventas por registro: ${promedio:.2f}")
        print(f"Vendedor Estrella: {mejor_vendedor} (${totales_vendedor[mejor_vendedor]})")
        print(f"\nRanking exportado a '{archivo_out}'")

    except FileNotFoundError:
        print("Error: No se encontró el archivo de ventas.")
    except json.JSONDecodeError:
        print("Error: El archivo JSON está vacío o mal formado.")

analizar_ventas('ventas.json', 'ranking_ventas.json')