import json

def procesar_inventario(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            productos = json.load(f)

        valor_total_inventario = 0
        bajo_stock = []

        print(f"{'PRODUCTO':<20} | {'SUBTOTAL':<12}")
        print("-" * 35)

        for p in productos:
            subtotal = p['precio'] * p['cantidad']
            valor_total_inventario += subtotal
            
            print(f"{p['producto']:<20} | ${subtotal:>10.2f}")

            if p['cantidad'] < 5:
                bajo_stock.append(p)
        print("-" * 35)
        print(f"VALOR TOTAL DEL INVENTARIO: ${valor_total_inventario:.2f}")
        
        with open(archivo_salida, 'w', encoding='utf-8') as f_out:
            json.dump(bajo_stock, f_out, indent=4, ensure_ascii=False)
            
        print(f"\nArchivo '{archivo_salida}' generado con éxito.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_entrada}'.")

procesar_inventario('inventario.json', 'bajo_stock.json')