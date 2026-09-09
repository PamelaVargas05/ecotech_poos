from dominio.empleado import EmpleadoMensual, EmpleadoPorHora
from dominio.departamento import Departamento

if __name__ == "__main__":
    desarrollo = Departamento("Desarrollo de Software")

    # Instanciación de subclases
    ana = EmpleadoMensual("Ana Torres", "ana.torres@ecotech.cl", 1200000.0)
    carlos = EmpleadoPorHora("Carlos Gómez", "carlos.gomez@ecotech.cl", horas=160, valor_hora=8500.0)

    # 1. Prueba de operación permitida
    print("--- Operación Permitida ---")
    print("Agregando a Ana:", desarrollo.agregar_empleado(ana))      # Retorna True
    print("Agregando a Carlos:", desarrollo.agregar_empleado(carlos))  # Retorna True

    # 2. Prueba de operación rechazada (Regla de encapsulamiento)
    print("\n--- Operación Rechazada ---")
    print("Intentando agregar a Ana otra vez:", desarrollo.agregar_empleado(ana))  # Retorna False

    # 3. Demostración de Polimorfismo
    print("\n--- Cálculo Polimórfico de Pagos ---")
    print(f"Total empleados en {desarrollo.nombre}: {desarrollo.cantidad_empleados()}")
    for emp in desarrollo.empleados:
        print(f"- {emp.mostrar_datos()} | Pago: ${emp.calcular_pago():,.0f}")