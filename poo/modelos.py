class Contrato:
    def __init__(self, tipo, duracion):
        self.__tipo = tipo
        self.__duracion = duracion

    def get_detalles(self):
        return f"Contrato {self.__tipo} ({self.__duracion})"

class Empleado:
    def __init__(self, id_emp, nombre, salario_base):
        self.__id_emp = id_emp
        self.__nombre = nombre
        self.__salario_base = salario_base
        self.__contrato = None

#uso getters y setters los cuales no vimos como tal en clase pero son importantes

    def get_nombre(self): return self.__nombre
    def get_salario_base(self): return self.__salario_base
    def set_contrato(self, contrato): self.__contrato = contrato
    def get_contrato_info(self):
        return self.__contrato.get_detalles() if self.__contrato else "Sin contrato"

    def calcular_pago(self):
        pass

class Administrativo(Empleado):
    def __init__(self, id_emp, nombre, salario_base, bono):
        super().__init__(id_emp, nombre, salario_base)
        self.__bono = bono

    def calcular_pago(self):
        return self.get_salario_base() + self.__bono

class Operativo(Empleado):
    def __init__(self, id_emp, nombre, salario_base, horas_extra):
        super().__init__(id_emp, nombre, salario_base)
        self.__horas_extra = horas_extra

    def calcular_pago(self):
        return self.get_salario_base() + (self.__horas_extra * 25.0)

class Departamento:
    def __init__(self, nombre_depto):
        self.__nombre_depto = nombre_depto
        self.__empleados = []

    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)

    def get_nombre(self): return self.__nombre_depto
    def get_empleados(self): return self.__empleados

class Empresa:
    def __init__(self, nombre_empresa):
        self.__nombre_empresa = nombre_empresa
        self.__departamentos = []

    def agregar_depto(self, depto):
        self.__departamentos.append(depto)

    def mostrar_nomina_total(self):
        print(f"--- NÓMINA DE {self.__nombre_empresa.upper()} ---")
        for depto in self.__departamentos:
            print(f"\nDepto: {depto.get_nombre()}")
            for emp in depto.get_empleados():
                print(f" > {emp.get_nombre()} | {emp.get_contrato_info()} | Total: ${emp.calcular_pago()}")