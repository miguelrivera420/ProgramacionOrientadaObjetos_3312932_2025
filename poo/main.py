from modelos import Empresa, Departamento, Administrativo, Operativo, Contrato

if __name__ == "__main__":
    
    empresa_global = Empresa("Tech Solutions")
    area_ventas = Departamento("Ventas")

    juan = Administrativo("A1", "Juan Perez", 2500, 300)
    contrato_juan = Contrato("Indefinido", "N/A")
    juan.set_contrato(contrato_juan)
    
    maria = Operativo("O1", "Maria Lopez", 1200, 15)
    contrato_maria = Contrato("Temporal", "3 meses")
    maria.set_contrato(contrato_maria)
    
    area_ventas.agregar_empleado(juan)
    area_ventas.agregar_empleado(maria)
    empresa_global.agregar_depto(area_ventas)
    
    empresa_global.mostrar_nomina_total()