import csv

total_inventario = 0


with open('inventario.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    
    # no lo vimos en clase, pero sirve para saltar la primera linea del archivo y asi porder multiplicar.
    next(lector)
    
    for fila in lector:
        codigo = fila[0]
        nombre = fila[1]
        precio = int(fila[2])
        cantidad = int(fila[3])
        
        subtotal = precio * cantidad
        total_inventario = total_inventario + subtotal
        
        print(f"Código: {codigo} | Nombre: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

print("VALOR TOTAL DEL INVENTARIO:", total_inventario)