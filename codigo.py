from tabulate import tabulate

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
    unidades_requeridas_1erp2dosem = produccion_unidades_1erp2dosem + inventario_final_deseado_1erp2dorsem - inventario_inicial_1erp2dosem
    total_unidades_producir_1erp = unidades_requeridas_1erp1ersem + unidades_requeridas_1erp2dosem
    # producto 2
    produccion_unidades_2dop1ersem = int(input("Ingrese la cantidad de unidades a producir del 2do producto en el primer semestre : "))
    inventario_final_deseado_2dop1ersem = int(input("Ingrese el inventario final deseado del 2do producto en el primer semestre : "))
    inventario_inicial_2dop1ersem = int(input("Ingrese el inventario inicial del 2do producto en el primer semestre : "))
    unidades_requeridas_2dop1ersem = produccion_unidades_2dop1ersem + inventario_final_deseado_2dop1ersem - inventario_inicial_2dop1ersem
    
    produccion_unidades_2dop2dosem = int(input("Ingrese la cantidad de unidades a producir del 2do producto en el segundo semestre : "))
    inventario_final_deseado_2dop2dorsem = int(input("Ingrese el inventario final deseado del 2do producto en el segundo semestre : "))
    inventario_inicial_2dop2dosem = int(input("Ingrese el inventario inicial del 2do producto en el segundo semestre : "))
    unidades_requeridas_2dop2dosem = produccion_unidades_2dop2dosem + inventario_final_deseado_2dop2dorsem - inventario_inicial_2dop2dosem
    total_unidades_producir_2dop = unidades_requeridas_2dop1ersem + unidades_requeridas_2dop2dosem
    #producto 3
    produccion_unidades_3erp1ersem = int(input("Ingrese la cantidad de unidades a producir del 3er producto en el primer semestre : "))
    inventario_final_deseado_3erp1ersem = int(input("Ingrese el inventario final deseado del 3er producto en el primer semestre : "))
    inventario_inicial_3erp1ersem = int(input("Ingrese el inventario inicial del 3er producto en el primer semestre : "))
    unidades_requeridas_3erp1ersem = produccion_unidades_3erp1ersem + inventario_final_deseado_3erp1ersem - inventario_inicial_3erp1ersem
    
    produccion_unidades_3erp2dosem = int(input("Ingrese la cantidad de unidades a producir del 3er producto en el segundo semestre : "))
    inventario_final_deseado_3erp2dorsem = int(input("Ingrese el inventario final deseado del 3er producto en el segundo semestre : "))
    inventario_inicial_3erp2dosem = int(input("Ingrese el inventario inicial del 3er producto en el segundo semestre : "))
    unidades_requeridas_3erp2dosem = produccion_unidades_3erp2dosem + inventario_final_deseado_3erp2dorsem - inventario_inicial_3erp2dosem
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

from tabulate import tabulate

# Tabla 4: Presupuesto de Requerimiento de Materiales
def presupuesto_requerimiento_de_materiales(mensaje):
  try:
    dato = float(input(mensaje))
    return dato
  except ValueError:
    print("Por favor, ingresa un número válido.")
    return presupuesto_requerimiento_de_materiales(mensaje)

# Pedir los datos necesarios para el presupuesto de requerimiento de materiales
print("\n1er SEMESTRE")
print("\nPRODUCTO 1")
unidades_1_1 = presupuesto_requerimiento_de_materiales("Ingresa las unidades a producir: ")
req_a_1_1 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material A: ")
req_b_1_1 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material B: ")
req_c_1_1 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material C: ")
print("\nPRODUCTO 2")
unidades_2_1 = presupuesto_requerimiento_de_materiales("Ingresa las unidades a producir: ")
req_a_2_1 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material A: ")
req_b_2_1 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material B: ")
req_c_2_1 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material C: ")
print("\nPRODUCTO 3")
unidades_3_1 = presupuesto_requerimiento_de_materiales("Ingresa las unidades a producir: ")
req_a_3_1 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material A: ")
req_b_3_1 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material B: ")
req_c_3_1 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material C: ")

# Calcular los valores del 1er. semestre para el presupuesto de requerimiento de materiales
total_a_1_1 = unidades_1_1 * req_a_1_1
total_b_1_1 = unidades_1_1 * req_b_1_1
total_c_1_1 = unidades_1_1 * req_c_1_1

total_a_2_1 = unidades_2_1 * req_a_2_1
total_b_2_1 = unidades_2_1 * req_b_2_1
total_c_2_1 = unidades_2_1 * req_c_2_1

total_a_3_1 = unidades_3_1 * req_a_3_1
total_b_3_1 = unidades_3_1 * req_b_3_1
total_c_3_1 = unidades_3_1 * req_c_3_1

total_a_1_4 = total_a_1_1 + total_a_2_1 + total_a_3_1
total_b_1_4 = total_b_1_1 + total_b_2_1 + total_b_3_1
total_c_1_4 = total_c_1_1 + total_c_2_1 + total_c_3_1

# Pedir los datos necesarios del 2do. semestre para el presupuesto de requerimiento de materiales
print("\n2do SEMESTRE")
print("\nPRODUCTO 1")
unidades_1_2 = presupuesto_requerimiento_de_materiales("Ingresa las unidades a producir: ")
req_a_1_2 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material A: ")
req_b_1_2 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material B: ")
req_c_1_2 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material C: ")
print("\nPRODUCTO 2")
unidades_2_2 = presupuesto_requerimiento_de_materiales("Ingresa las unidades a producir: ")
req_a_2_2 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material A: ")
req_b_2_2 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material B: ")
req_c_2_2 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material C: ")
print("\nPRODUCTO 3")
unidades_3_2 = presupuesto_requerimiento_de_materiales("Ingresa las unidades a producir: ")
req_a_3_2 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material A: ")
req_b_3_2 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material B: ")
req_c_3_2 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material C: ")

total_a_1_2 = unidades_1_2 * req_a_1_2
total_b_1_2 = unidades_1_2 * req_b_1_2
total_c_1_2 = unidades_1_2 * req_c_1_2

total_a_2_2 = unidades_2_2 * req_a_2_2
total_b_2_2 = unidades_2_2 * req_b_2_2
total_c_2_2 = unidades_2_2 * req_c_2_2

total_a_3_2 = unidades_3_2 * req_a_3_2
total_b_3_2 = unidades_3_2 * req_b_3_2
total_c_3_2 = unidades_3_2 * req_c_3_2

total_a_2_4 = total_a_1_2 + total_a_2_2 + total_a_3_2
total_b_2_4 = total_b_1_2 + total_b_2_2 + total_b_3_2
total_c_2_4 = total_c_1_2 + total_c_2_2 + total_c_3_2

#Pedir los datos del año para el presupuesto de requerimiento de materiales
print("\n * AÑO *")
print("\nPRODUCTO 1")
unidades_1_3 = presupuesto_requerimiento_de_materiales("Ingresa las unidades a producir: ")
req_a_1_3 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material A: ")
req_b_1_3 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material B: ")
req_c_1_3 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material C: ")
print("\nPRODUCTO 2")
unidades_2_3 = presupuesto_requerimiento_de_materiales("Ingresa las unidades a producir: ")
req_a_2_3 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material A: ")
req_b_2_3 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material B: ")
req_c_2_3 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material C: ")
print("\nPRODUCTO 3")
unidades_3_3 = presupuesto_requerimiento_de_materiales("Ingresa las unidades a producir: ")
req_a_3_3 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material A: ")
req_b_3_3 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material B: ")
req_c_3_3 = presupuesto_requerimiento_de_materiales("Ingresa el requerimiento de material C: ")

total_a_1_3 = unidades_1_3 * req_a_1_3
total_b_1_3 = unidades_1_3 * req_b_1_3
total_c_1_3 = unidades_1_3 * req_c_1_3

total_a_2_3 = unidades_2_3 * req_a_2_3
total_b_2_3 = unidades_2_3 * req_b_2_3
total_c_2_3 = unidades_2_3 * req_c_2_3

total_a_3_3 = unidades_3_3 * req_a_3_3
total_b_3_3 = unidades_3_3 * req_b_3_3
total_c_3_3 = unidades_3_3 * req_c_3_3

total_a_3_4 = total_a_1_3 + total_a_2_3 + total_a_3_3
total_b_3_4 = total_b_1_3 + total_b_2_3 + total_b_3_3
total_c_3_4 = total_c_1_3 + total_c_2_3 + total_c_3_3

# Crear una lista de listas con los datos del presupuesto de requerimiento de materiales
datos_presupuesto_requerimiento_de_materiales= [
    ["PRODUCTO 1", "", "", ""],
    ["Unidades a producir", unidades_1_1, unidades_1_2, unidades_1_3],
    ["Material A", "", "", ""],
    ["Requerimiento de material", req_a_1_1, req_a_1_2, req_a_1_3],
    ["Total de Material A requerido", total_a_1_1, total_a_2_1, total_a_3_1],
    ["Material B", "", "", ""],
    ["Requerimiento de material", req_b_1_1, req_b_1_2, req_b_1_3],
    ["Total de Material B requerido", total_b_1_1, total_b_2_1, total_b_3_1],
    ["Material C", "", "", ""],
    ["Requerimiento de material", req_c_1_1, req_c_1_2, req_c_1_3],
    ["Total de Material C requerido", total_c_1_1, total_c_2_1, total_c_3_1],
    ["PRODUCTO 2", "", "", ""],
    ["Unidades a producir", unidades_2_1, unidades_2_2, unidades_2_3],
    ["Material A", "", "", ""],
    ["Requerimiento de material", req_a_2_1, req_a_2_2, req_a_2_3],
    ["Total de Material A requerido", total_a_2_1, total_a_2_2, total_a_2_3],
    ["Material B", "", "", ""],
    ["Requerimiento de material", req_b_2_1, req_b_2_2, req_b_2_3],
    ["Total de Material B requerido", total_b_2_1, total_b_2_2, total_b_2_3],
    ["Material C", "", "", ""],
    ["Requerimiento de material", req_c_2_1, req_c_2_2, req_c_2_3],
    ["Total de Material C requerido", total_c_2_1, total_c_2_2, total_c_2_3],
    ["PRODUCTO 3", "", "", ""],
    ["Unidades a producir", unidades_3_1, unidades_3_2, unidades_3_3],
    ["Material A", "", "", ""],
    ["Requerimiento de material", req_a_3_1, req_a_3_2, req_a_3_3],
    ["Total de Material A requerido", total_a_3_1, total_a_3_2, total_a_3_3],
    ["Material B", "", "", ""],
    ["Requerimiento de material", req_b_3_1, req_b_3_2, req_b_3_3],
    ["Total de Material B requerido", total_b_3_1, total_b_3_2, total_b_3_3],
    ["Material C", "", "", ""],
    ["Requerimiento de material", req_c_3_1, req_c_3_2, req_c_3_3],
    ["Total de Material C requerido", total_c_3_1, total_c_3_2, total_c_3_3],
    ["Total de Requerimientos", "", "", ""],
    ["Material A", total_a_1_4, total_a_2_4, total_a_3_4],
    ["Material B", total_b_1_4, total_b_2_4, total_b_3_4],
    ["Material C", total_c_1_4, total_c_2_4, total_c_3_4]
]

# Impresion de datos de presupuesto de requerimiento de materiales - Tabla 4
tabla = tabulate(datos_presupuesto_requerimiento_de_materiales, headers=["Producto", "1er. Semestre", "2do. Semestre", "Total Año"], tablefmt="grid")
# Mostrar la tabla
print("Presupuesto de Requerimiento de Materiales")
print(tabla)

# Tabla 5: Presupuesto de Compra de Materiales
def presupuesto_compra_de_materiales(mensaje):
  try:
    dato = float(input(mensaje))
    return dato
  except ValueError:
    print("Por favor, ingresa un número válido.")
    return presupuesto_requerimiento_de_materiales(mensaje)

# Pedir los datos necesarios para el presupuesto de compra de materiales
print("\n * 1er SEMESTRE *")
print("\nMaterial A")
inv_fin_a_1 = presupuesto_compra_de_materiales("\n Ingrese inventario final de material A: ")
inv_ini_a_1 = presupuesto_compra_de_materiales("\n Ingrese inventario inicial de material A: ")
pre_com_a_1 = presupuesto_compra_de_materiales("\n Ingrese precio de compra de material A: ")
print("\nMaterial B")
inv_fin_b_1 = presupuesto_compra_de_materiales("\n Ingrese inventario final de material B: ")
inv_ini_b_1 = presupuesto_compra_de_materiales("\n Ingrese inventario inicial de material B: ")
pre_com_b_1 = presupuesto_compra_de_materiales("\n Ingrese precio de compra de material B: ")
print("\nMaterial C")
inv_fin_c_1 = presupuesto_compra_de_materiales("\n Ingrese inventario final de material C: ")
inv_ini_c_1 = presupuesto_compra_de_materiales("\n Ingrese inventario inicial de material C: ")
pre_com_c_1 = presupuesto_compra_de_materiales("\n Ingrese precio de compra de material C: ")

# Calcular los valores del 1er. semestre para el presupuesto de compra de materiales
total_m_1 = total_a_1_4 + inv_fin_a_1
mat_com_a_1 = total_m_1 - inv_ini_a_1
total_m_a_1 = mat_com_a_1 * pre_com_a_1

total_m_2 = total_b_1_4 + inv_fin_b_1
mat_com_b_1 = total_m_2 - inv_ini_b_1
total_m_b_1 = mat_com_b_1 * pre_com_b_1

total_m_3 = total_c_1_4 + inv_fin_c_1
mat_com_c_1 = total_m_3 - inv_ini_c_1
total_m_c_1 = mat_com_c_1 * pre_com_c_1

com_total_1 = total_m_a_1 + total_m_b_1 + total_m_c_1

# Pedir los datos necesarios del 2do. semestre para el presupuesto de compra de materiales
print("\n * 2do SEMESTRE *")
print("\nMaterial A")
inv_fin_a_2 = presupuesto_compra_de_materiales("\n Ingrese inventario final de material A: ")
inv_ini_a_2 = presupuesto_compra_de_materiales("\n Ingrese inventario inicial de material A: ")
pre_com_a_2 = presupuesto_compra_de_materiales("\n Ingrese precio de compra de material A: ")
print("\nMaterial B")
inv_fin_b_2 = presupuesto_compra_de_materiales("\n Ingrese inventario final de material B: ")
inv_ini_b_2 = presupuesto_compra_de_materiales("\n Ingrese inventario inicial de material B: ")
pre_com_b_2 = presupuesto_compra_de_materiales("\n Ingrese precio de compra de material B: ")
print("\nMaterial C")
inv_fin_c_2 = presupuesto_compra_de_materiales("\n Ingrese inventario final de material C: ")
inv_ini_c_2 = presupuesto_compra_de_materiales("\n Ingrese inventario inicial de material C: ")
pre_com_c_2 = presupuesto_compra_de_materiales("\n Ingrese precio de compra de material C: ")

total_m_a_2 = total_a_2_4 + inv_fin_a_2
mat_com_a_2 = total_m_a_2 - inv_ini_a_2
total_m_a_2_5 = mat_com_a_2 * pre_com_a_2

total_m_b_2 = total_b_2_4 + inv_fin_b_2
mat_com_b_2 = total_m_b_2 - inv_ini_b_2
total_m_b_2_5 = mat_com_b_2 * pre_com_b_2

total_m_c_2 = total_c_2_4 + inv_fin_c_2
mat_com_c_2 = total_m_c_2 - inv_ini_c_2
total_m_c_2_5 = mat_com_c_2 * pre_com_c_2

com_total_2 = total_m_a_2_5 + total_m_b_2_5 + total_m_c_2_5

# Pedir los datos del año para el presupuesto de compra de materiales
print("\n * AÑO *")
print("\nMaterial A")
inv_fin_a_3 = presupuesto_compra_de_materiales("\n Ingrese inventario final de material A: ")
inv_ini_a_3 = presupuesto_compra_de_materiales("\n Ingrese inventario inicial de material A: ")
print("\nMaterial B")
inv_fin_b_3 = presupuesto_compra_de_materiales("\n Ingrese inventario final de material B: ")
inv_ini_b_3 = presupuesto_compra_de_materiales("\n Ingrese inventario inicial de material B: ")
print("\nMaterial C")
inv_fin_c_3 = presupuesto_compra_de_materiales("\n Ingrese inventario final de material C: ")
inv_ini_c_3 = presupuesto_compra_de_materiales("\n Ingrese inventario inicial de material C: ")

total_m_a_3 = total_a_3_4 + inv_fin_a_3
mat_com_a_3 = total_m_a_3 - inv_ini_a_3
total_m_a_3_5 = total_m_a_1 + total_m_a_2_5

total_m_b_3 = total_b_3_4 + inv_fin_b_3
mat_com_b_3 = total_m_b_3 - inv_ini_b_3
total_m_b_3_5 = total_m_b_1 + total_m_b_2_5

total_m_c_3 = total_c_3_4 + inv_fin_c_3
mat_com_c_3 = total_m_c_3 - inv_ini_c_3
total_m_c_3_5 = total_m_c_1 + total_m_c_2_5

com_total_3 = total_m_a_3_5 + total_m_b_3_5 + total_m_c_3_5

# Crear una lista de listas con los datos del presupuesto de compra de materiales
datos_presupuesto_compra_de_materiales= [
    ["Material A", "", "", ""],
    ["Requerimiento de materiales", total_a_1_4, total_a_2_4, total_a_3_4],
    ["Inventario final", inv_fin_a_1, inv_fin_a_2, inv_fin_a_3],
    ["Total de materiales", total_m_1, total_m_a_2, total_m_a_3],
    ["Inventario inicial", inv_ini_a_1, inv_ini_a_2, inv_ini_a_3],
    ["Material a comprar", mat_com_a_1, mat_com_a_2, mat_com_a_3],
    ["Precio de compra", pre_com_a_1, pre_com_a_2, ""],
    ["Total de material A en $", total_m_a_1, total_m_a_2_5, total_m_a_3_5],
    ["Material B", "", "", ""],
    ["Requerimiento de materiales", total_b_1_4, total_b_2_4, total_b_3_4],
    ["Inventario final", inv_fin_b_1, inv_fin_b_2, inv_fin_b_3],
    ["Total de materiales requeridos", total_m_2, total_m_b_2, total_m_b_3],
    ["Inventario inicial", inv_ini_b_1, inv_ini_b_2, inv_ini_b_3],
    ["Materiales a comprar", mat_com_b_1, mat_com_b_2, mat_com_b_3],
    ["Precio de compra", pre_com_b_1, pre_com_b_2, ""],
    ["Total de compra de materiales", total_m_b_1, total_m_b_2_5, total_m_b_3_5],
    ["Material C", "", "", ""],
    ["Requerimiento de materiales", total_c_1_4, total_c_2_4, total_c_3_4],
    ["Inventario final", inv_fin_c_1, inv_fin_c_2, inv_fin_c_3],
    ["Total de materiales requeridos", total_m_3, total_m_c_2, total_m_c_3],
    ["Inventario inicial", inv_ini_c_1, inv_ini_c_2, inv_ini_c_3],
    ["Materiales a comprar", mat_com_c_1, mat_com_c_2, mat_com_c_3],
    ["Precio de compra", pre_com_c_1, pre_com_c_2, ""],
    ["Total de compra de materiales C en $", total_m_c_1, total_m_c_2_5, total_m_c_3_5],
    ["Compras totales", com_total_1, com_total_2, com_total_3]
]

# Impresion de datos de determinacion del saldo de proveedores y flujo de salida - Tabla 6
tabla = tabulate(datos_presupuesto_compra_de_materiales, headers=["", "1er. Semestre", "2do. Semestre", "Total año"], tablefmt="grid")
# Mostrar la tabla
print("\nPresupuesto compra de materiales")
print(tabla)

# Tabla 6: Determinacion del saldo de Proveedores y Flujo de Salidas
def determinacion_saldo_proveedores_flujo_salida (mensaje):
  try:
    dato = float(input(mensaje))
    return dato
  except ValueError:
    print("Por favor, ingresa un número válido.")
    return determinacion_saldo_proveedores_flujo_salida(mensaje)

# Pedir los datos necesarios para la determinacion del saldo de proveedores y flujo de salida
print("\n Determinacion del saldo de Proveedores y Flujo de Salidas")
saldo_proveedores_31_dic_año = determinacion_saldo_proveedores_flujo_salida("\nIngrese el saldo de proveedores al 31 de diciembre del año: ")

compras_año = com_total_3
total_proveedores = compras_año + saldo_proveedores_31_dic_año
por_proveedor_año1 = com_total_3 * 0.5
total_salidas_año = saldo_proveedores_31_dic_año + por_proveedor_año1
saldo_proveedores_año = total_proveedores - total_salidas_año

# Crear una lista de listas con los datos de la determinacion del saldo de proveedores y flujo de salida
datos_determinacion_saldo_proveedores_flujo_salida= [
    ["Saldo de Proveedores al 31 de diciembre del año","", saldo_proveedores_31_dic_año],
    ["Compras del año", "", compras_año],
    ["Total de Proveedores", "", total_proveedores],
    ["Por Proveedor del año", saldo_proveedores_31_dic_año, ""],
    ["Por Proveedor del año 1", por_proveedor_año1, ""],
    ["Total de Salidas del año", "", total_salidas_año],
    ["Saldo de Proveedores del año", "", saldo_proveedores_año]
]

# Impresion de datos de determinacion del saldo de proveedores y flujo de salida - Tabla 6
tabla = tabulate(datos_determinacion_saldo_proveedores_flujo_salida, headers=["Descripcion", "Importe", "Total"], tablefmt="grid")
# Mostrar la tabla
print("Determinacion del saldo de Proveedores y Flujo de Salidas")
print(tabla)