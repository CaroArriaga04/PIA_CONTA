# Presupuesto maestro
# Tabla 1: Presupuesto de Ventas
def presupuesto_ventas():
    unidades_vender = int(input("Ingrese la cantidad de unidades a vender: "))
    precio_venta = float(input("Ingrese el precio de venta por unidad: "))
    total_ventas = unidades_vender * precio_venta
    return total_ventas

# Tabla 2: Saldo de Clientes y Flujo de Entradas
def saldo_clientes():
    saldo_clientes_31_dic_2022 = float(input("Ingrese el saldo de clientes al 31 de diciembre de 2022: "))
    ventas_2023 = presupuesto_ventas()
    total_clientes_2023 = saldo_clientes_31_dic_2022 + ventas_2023

    por_cobranza_2022 = float(input("Ingrese el monto por cobranza del 2022: "))
    por_cobranza_2023 = float(input("Ingrese el monto por cobranza del 2023: "))
    total_entradas = por_cobranza_2022 + por_cobranza_2023

    saldo_clientes_2023 = total_clientes_2023 - total_entradas

    return saldo_clientes_31_dic_2022, ventas_2023, total_clientes_2023, por_cobranza_2022, por_cobranza_2023, total_entradas, saldo_clientes_2023


# Tabla 3: Presupuesto de Producción
def presupuesto_produccion():
    produccion_unidades = int(input("Ingrese la cantidad de unidades a producir(lo mismo de unidades a vender): "))
    inventario_final_deseado = int(input("Ingrese el inventario final deseado: "))
    inventario_inicial = int(input("Ingrese el inventario inicial: "))
    unidades_requeridas = produccion_unidades + inventario_final_deseado - inventario_inicial
    return unidades_requeridas

# Mostrar los resultados

total_ventas = presupuesto_ventas()
print(f"\nPresupuesto de Ventas: ${total_ventas:.2f}\n")

saldo_31_dic_2022, ventas_2023, total_clientes_2023, cobranza_2022, cobranza_2023, total_entradas_2023, saldo_2023 = saldo_clientes()

print(f"\nSaldo de Clientes al 31 de diciembre de 2022: ${saldo_31_dic_2022:.2f}")
print(f"Ventas 2023: ${ventas_2023:.2f}")
print(f"Total de Clientes 2023: ${total_clientes_2023:.2f}")
print(f"Por cobranza del 2022: ${cobranza_2022:.2f}")
print(f"Por cobranza del 2023: ${cobranza_2023:.2f}")
print(f"Total de Entradas 2023: ${total_entradas_2023:.2f}")
print(f"Saldo de Clientes 2023: ${saldo_2023:.2f}\n")

unidades_requeridas = presupuesto_produccion()
print(f"Unidades a Producir: {unidades_requeridas} unidades\n")

