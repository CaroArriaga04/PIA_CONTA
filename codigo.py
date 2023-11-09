# Presupuesto maestro
# Tabla 1: Presupuesto de Ventas
def presupuesto_ventas():
    unidades_vender_1ersem = int(input("Ingrese la cantidad de unidades a vender del primer semestre: "))
    precio_venta_1ersem = float(input("Ingrese el precio de venta por unidad del primer semestre: "))
    total_ventas_1ersem = unidades_vender_1ersem * precio_venta_1ersem
    unidades_vender_2dosem = int(input("Ingrese la cantidad de unidades a vender del segundo semestre: "))
    precio_venta_2dosem = float(input("Ingrese el precio de venta por unidad del segundo semestre: "))
    total_ventas_2dosem = unidades_vender_2dosem * precio_venta_2dosem
    return total_ventas_1ersem, total_ventas_2dosem

# Tabla 2: Saldo de Clientes y Flujo de Entradas
def saldo_clientes():
    saldo_clientes_31_dic_2022 = float(input("Ingrese el saldo de clientes al 31 de diciembre de 2022: "))
    ventas_2023 = presupuesto_ventas()

    total_clientes_2023 = saldo_clientes_31_dic_2022 + sum(ventas_2023)

    por_cobranza_2022 = float(input("Ingrese el monto por cobranza del 2022: "))
    por_cobranza_2023 = float(input("Ingrese el monto por cobranza del 2023: "))
    total_entradas = por_cobranza_2022 + por_cobranza_2023

    saldo_clientes_2023 = total_clientes_2023 - total_entradas

    return saldo_clientes_31_dic_2022, ventas_2023, total_clientes_2023, por_cobranza_2022, por_cobranza_2023, total_entradas, saldo_clientes_2023

# Tabla 3: Presupuesto de Producción
def presupuesto_produccion():
    #producto 1
    produccion_unidades_1erp1ersem = int(input("Ingrese la cantidad de unidades a producir del 1er producto en el primer semestre : "))
    inventario_final_deseado_1erp1ersem = int(input("Ingrese el inventario final deseado del 1er producto en el primer semestre : "))
    inventario_inicial_1erp1ersem = int(input("Ingrese el inventario inicial del 1er producto en el primer semestre : "))
    unidades_requeridas_1erp1ersem = produccion_unidades_1erp1ersem + inventario_final_deseado_1erp1ersem - inventario_inicial_1erp1ersem
    
    produccion_unidades_1erp2dosem = int(input("Ingrese la cantidad de unidades a producir del 1er producto en el segundo semestre : "))
    inventario_final_deseado_1erp2dorsem = int(input("Ingrese el inventario final deseado del 1er producto en el segundo semestre : "))
    inventario_inicial_1erp2dosem = int(input("Ingrese el inventario inicial del 1er producto en el segundo semestre : "))
    unidades_requeridas_1erp2dosem = produccion_unidades_1erp2dosem + inventario_final_deseado_1erp2dosem - inventario_inicial_1erp2dosem
    total_unidades_producir_1erp = unidades_requeridas_1erp1ersem + unidades_requeridas_1erp2dosem
    # producto 2
    produccion_unidades_2dop1ersem = int(input("Ingrese la cantidad de unidades a producir del 2do producto en el primer semestre : "))
    inventario_final_deseado_2dop1ersem = int(input("Ingrese el inventario final deseado del 2do producto en el primer semestre : "))
    inventario_inicial_2dop1ersem = int(input("Ingrese el inventario inicial del 2do producto en el primer semestre : "))
    unidades_requeridas_2dop1ersem = produccion_unidades_2dop1ersem + inventario_final_deseado_2dop1ersem - inventario_inicial_2dop1ersem
    
    produccion_unidades_2dop2dosem = int(input("Ingrese la cantidad de unidades a producir del 2do producto en el segundo semestre : "))
    inventario_final_deseado_2dop2dorsem = int(input("Ingrese el inventario final deseado del 2do producto en el segundo semestre : "))
    inventario_inicial_2dop2dosem = int(input("Ingrese el inventario inicial del 2do producto en el segundo semestre : "))
    unidades_requeridas_2dop2dosem = produccion_unidades_2dop2dosem + inventario_final_deseado_2dop2dosem - inventario_inicial_2dop2dosem
    total_unidades_producir_2dop = unidades_requeridas_2dop1ersem + unidades_requeridas_2dop2dosem
    #producto 3
    produccion_unidades_3erp1ersem = int(input("Ingrese la cantidad de unidades a producir del 3er producto en el primer semestre : "))
    inventario_final_deseado_3erp1ersem = int(input("Ingrese el inventario final deseado del 3er producto en el primer semestre : "))
    inventario_inicial_3erp1ersem = int(input("Ingrese el inventario inicial del 3er producto en el primer semestre : "))
    unidades_requeridas_3erp1ersem = produccion_unidades_3erp1ersem + inventario_final_deseado_3erp1ersem - inventario_inicial_3erp1ersem
    
    produccion_unidades_3erp2dosem = int(input("Ingrese la cantidad de unidades a producir del 3er producto en el segundo semestre : "))
    inventario_final_deseado_3erp2dorsem = int(input("Ingrese el inventario final deseado del 3er producto en el segundo semestre : "))
    inventario_inicial_3erp2dosem = int(input("Ingrese el inventario inicial del 3er producto en el segundo semestre : "))
    unidades_requeridas_3erp2dosem = produccion_unidades_3erp2dosem + inventario_final_deseado_3erp2dosem - inventario_inicial_3erp2dosem
    total_unidades_producir_3erp = unidades_requeridas_3erp1ersem + unidades_requeridas_3erp2dosem
    
    return total_unidades_producir_1erp, total_unidades_producir_2dop, total_unidades_producir_3erp


# Mostrar los resultados

total_ventas_1ersem, total_ventas_2dosem = presupuesto_ventas()
total_ventas = total_ventas_1ersem + total_ventas_2dosem
print(f"\nPresupuesto de Ventas: ${total_ventas:.2f}\n")

saldo_31_dic_2022, ventas_2023, total_clientes_2023, cobranza_2022, cobranza_2023, total_entradas_2023, saldo_2023 = saldo_clientes()
ventas_2023_1ersem, ventas_2023_2dosem = ventas_2023

print(f"\nSaldo de Clientes al 31 de diciembre de 2022: ${saldo_31_dic_2022:.2f}")
print(f"Ventas 2023 Primer Semestre: ${ventas_2023_1ersem:.2f}")
print(f"Ventas 2023 Segundo Semestre: ${ventas_2023_2dosem:.2f}")
print(f"Total de Clientes 2023: ${total_clientes_2023:.2f}")
print(f"Por cobranza del 2022: ${cobranza_2022:.2f}")
print(f"Por cobranza del 2023: ${cobranza_2023:.2f}")
print(f"Total de Entradas 2023: ${total_entradas_2023:.2f}")
print(f"Saldo de Clientes 2023: ${saldo_2023:.2f}\n")

unidades_1erp, unidades_2dop, unidades_3erp = presupuesto_produccion()
print(f"Unidades a Producir Producto 1: {unidades_1erp} unidades")
print(f"Unidades a Producir Producto 2: {unidades_2dop} unidades")
print(f"Unidades a Producir Producto 3: {unidades_3erp} unidades\n")