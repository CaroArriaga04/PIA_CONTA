# Presupuesto maestro
# Tabla 1: Presupuesto de Ventas
def presupuesto_ventas():
    unidades_vender = int(input("Ingrese la cantidad de unidades a vender: "))
    precio_venta = float(input("Ingrese el precio de venta por unidad: "))
    total_ventas = unidades_vendidas * precio_venta
    return total_ventas

# Tabla 2: Saldo de Clientes y Flujo de Entradas
def saldo_clientes():
    ventas_credito = float(input("Ingrese el porcentaje de ventas a crédito (en decimal): "))
    cobros_mes_siguiente = float(input("Ingrese el porcentaje de cobros el mes siguiente (en decimal): "))
    saldo_clientes = presupuesto_ventas() * ventas_credito
    cobros_efectivo = presupuesto_ventas() - saldo_clientes
    cobros_totales = cobros_efectivo + (presupuesto_ventas() * cobros_mes_siguiente)
    return saldo_clientes, cobros_totales

# Tabla 3: Presupuesto de Producción
def presupuesto_produccion():
    produccion_unidades = unidades_vender
    inventario_final_deseado = int(input("Ingrese el inventario final deseado: "))
    inventario_inicial = int(input("Ingrese el inventario inicial: "))
    unidades_requeridas = produccion_unidades + inventario_final_deseado - inventario_inicial
    return unidades_requeridas

# Mostrar los resultados
total_ventas = presupuesto_ventas()
print(f"\nPresupuesto de Ventas: ${total_ventas:.2f}\n")

saldo_clientes, cobros_totales = saldo_clientes()
print(f"Saldo de Clientes: ${saldo_clientes:.2f}")
print(f"Flujo de Entradas por Ventas: ${cobros_totales:.2f}\n")

unidades_requeridas = presupuesto_produccion()
print(f"Unidades a Producir: {unidades_requeridas} unidades\n")
