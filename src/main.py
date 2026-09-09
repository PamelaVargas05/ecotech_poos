from dominio.empleado import Empleado
from dominio.departamento import Departamento

if __name__ == "__main__":
    desarrollo = Departamento("Desarrollo de Software")
    ana = Empleado("Ana Torres", "ana.torres@ecotech.cl")
    carlos = Empleado("Carlos Gómez", "carlos.gomez@ecotech.cl")

    desarrollo.agregar_empleado(ana)
    desarrollo.agregar_empleado(carlos)

    print(f"Departamento: {desarrollo.nombre}")
    print(f"Total empleados: {desarrollo.cantidad_empleados()}")
    for emp in desarrollo.empleados:
        print(f"- {emp.mostrar_datos()}")