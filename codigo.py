from tabulate import tabulate

# Presupuesto maestro
# Tabla 1: Presupuesto de Ventas
def presupuesto_ventas(mensaje):
  try:
    dato = float(input(mensaje))
    return dato
  except ValueError:
    print("Por favor, ingresa un número válido.")
    return presupuesto_ventas(mensaje)

print("\nPRODUCTO 1")
unidades_vender_1erp1sem = presupuesto_ventas("Ingrese la cantidad de unidades a vender del primer semestre: ")
precio_venta_1erp1sem = presupuesto_ventas("Ingrese el precio de venta por unidad del primer semestre: ")
total_ventas_1erp1sem = unidades_vender_1erp1sem * precio_venta_1erp1sem

unidades_vender_1erp2sem = presupuesto_ventas("Ingrese la cantidad de unidades a vender del segundo semestre: ")
precio_venta_1erp2sem = presupuesto_ventas("Ingrese el precio de venta por unidad del segundo semestre: ")
total_ventas_1erp2sem = unidades_vender_1erp2sem * precio_venta_1erp2sem

total_ventas_1p = total_ventas_1erp1sem + total_ventas_1erp2sem

print("\nPRODUCTO 2")
unidades_vender_2dop1sem = presupuesto_ventas("Ingrese la cantidad de unidades a vender del primer semestre: ")
precio_venta_2dop1sem = presupuesto_ventas("Ingrese el precio de venta por unidad del primer semestre: ")
total_ventas_2dop1sem = unidades_vender_2dop1sem * precio_venta_2dop1sem

unidades_vender_2dop2sem = presupuesto_ventas("Ingrese la cantidad de unidades a vender del segundo semestre: ")
precio_venta_2dop2sem = presupuesto_ventas("Ingrese el precio de venta por unidad del segundo semestre: ")
total_ventas_2dop2sem = unidades_vender_2dop2sem * precio_venta_2dop2sem

total_ventas_2p = total_ventas_2dop1sem + total_ventas_2dop2sem

print("\nPRODUCTO 3")
unidades_vender_3erp1sem = presupuesto_ventas("Ingrese la cantidad de unidades a vender del primer semestre: ")
precio_venta_3erp1sem = presupuesto_ventas("Ingrese el precio de venta por unidad del primer semestre: ")
total_ventas_3erp1sem = unidades_vender_3erp1sem * precio_venta_3erp1sem

unidades_vender_3erp2sem = presupuesto_ventas("Ingrese la cantidad de unidades a vender del segundo semestre: ")
precio_venta_3erp2sem = presupuesto_ventas("Ingrese el precio de venta por unidad del segundo semestre: ")
total_ventas_3erp2sem = unidades_vender_3erp2sem * precio_venta_3erp2sem

total_ventas_3p = total_ventas_3erp1sem + total_ventas_3erp2sem
total_ventas_1sem = total_ventas_1erp1sem + total_ventas_2dop1sem + total_ventas_3erp1sem
total_ventas_2sem = total_ventas_1erp2sem + total_ventas_2dop2sem + total_ventas_3erp2sem
total_ventas_año = total_ventas_1sem + total_ventas_2sem 
  
# Crear una lista de listas con los datos del presupuesto de requerimiento de materiales
datos_presupuesto_ventas= [
    ["PRODUCTO 1", "", "", ""],
    ["Unidades a vender", unidades_vender_1erp1sem, unidades_vender_2dop1sem , ""],
    ["Precio de venta", precio_venta_1erp1sem , precio_venta_1erp2sem , ""],
    ["Importe de venta", total_ventas_1erp1sem , total_ventas_1erp2sem , total_ventas_1p],
    ["PRODUCTO 2", "", "", ""],
    ["Unidades a vender", unidades_vender_2dop1sem, unidades_vender_2dop2sem , ""],
    ["Precio de venta", precio_venta_2dop1sem , precio_venta_2dop2sem , ""],
    ["Importe de venta", total_ventas_2dop1sem , total_ventas_2dop2sem, total_ventas_2p],
    ["PRODUCTO 3", "", "", ""],
    ["Unidades a vender", unidades_vender_3erp1sem, unidades_vender_3erp2sem, ""],
    ["Precio de venta", precio_venta_3erp1sem, precio_venta_3erp2sem, ""],
    ["Importe de venta", total_ventas_3erp1sem, total_ventas_3erp2sem, total_ventas_3p],
    ["Total de ventas por semestre", total_ventas_1sem , total_ventas_2sem, total_ventas_año ]
]

# Impresion de datos de presupuesto de requerimiento de materiales - Tabla 1
tabla = tabulate(datos_presupuesto_ventas, headers=["Producto", "1er. Semestre", "2do. Semestre", "Total Año"], tablefmt="grid")
# Mostrar la tabla
print("Presupuesto de ventas")
print(tabla)


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
# Crear una lista de listas con los datos del presupuesto de requerimiento de materiales
datos_saldo_clientes= [
    ["Saldo de clientes 31-DIC-2022", "", saldo_clientes_31_dic_2022],
    ["Ventas 2023", "", ventas_2023],
    ["Total de clientes 2023", "" , total_clientes_2023],
    ["Entradas de Efectivo", "" , "",],
    ["Por cobranza del 2022", por_cobranza_2022 , ""],
    ["Por cobranza del  2023", por_cobranza_2023 , ""],
    ["Total de Entradas 2023", "", total_entradas],
    ["Saldo de clientes del 2023", "" , saldo_clientes_2023]
]

# Impresion de datos de presupuesto de requerimiento de materiales - Tabla 2
tabla = tabulate(datos_saldo_clientes, headers=["Descripción", "Importe", "Total"], tablefmt="grid")
# Mostrar la tabla
print("Saldo de Clientes")
print(tabla)

# Tabla 3: Presupuesto de Producción
def presupuesto_produccion():
    #producto 1
    produccion_unidades_1erp1ersem = int(input("Ingrese la cantidad de unidades a producir del 1er producto en el primer semestre : "))
    inventario_final_deseado_1erp1ersem = int(input("Ingrese el inventario final deseado del 1er producto en el primer semestre : "))
    total_unidades_1erp1ersem = produccion_unidades_1erp1ersem + inventario_final_deseado_1erp1ersem
    inventario_inicial_1erp1ersem = int(input("Ingrese el inventario inicial del 1er producto en el primer semestre : "))
    unidades_requeridas_1erp1ersem = produccion_unidades_1erp1ersem + inventario_final_deseado_1erp1ersem - inventario_inicial_1erp1ersem
    
    produccion_unidades_1erp2dosem = int(input("Ingrese la cantidad de unidades a producir del 1er producto en el segundo semestre : "))
    inventario_final_deseado_1erp2dosem = int(input("Ingrese el inventario final deseado del 1er producto en el segundo semestre : "))
    total_unidades_1erp2dosem = produccion_unidades_1erp2dosem + inventario_final_deseado_1erp2dosem
    inventario_inicial_1erp2dosem = int(input("Ingrese el inventario inicial del 1er producto en el segundo semestre : "))
    unidades_requeridas_1erp2dosem = produccion_unidades_1erp2dosem + inventario_final_deseado_1erp2dorsem - inventario_inicial_1erp2dosem
    total_unidades_producir_1erp = unidades_requeridas_1erp1ersem + unidades_requeridas_1erp2dosem
    total_unidades_1erp = total_unidades_1erp1ersem + total_unidades_1erp2dosem
    
    # producto 2
    produccion_unidades_2dop1ersem = int(input("Ingrese la cantidad de unidades a producir del 2do producto en el primer semestre : "))
    inventario_final_deseado_2dop1ersem = int(input("Ingrese el inventario final deseado del 2do producto en el primer semestre : "))
    total_unidades_2dop1ersem = produccion_unidades_2dop1ersem + inventario_final_deseado_2dop1ersem
    inventario_inicial_2dop1ersem = int(input("Ingrese el inventario inicial del 2do producto en el primer semestre : "))
    unidades_requeridas_2dop1ersem = produccion_unidades_2dop1ersem + inventario_final_deseado_2dop1ersem - inventario_inicial_2dop1ersem
    
    produccion_unidades_2dop2dosem = int(input("Ingrese la cantidad de unidades a producir del 2do producto en el segundo semestre : "))
    inventario_final_deseado_2dop2dorsem = int(input("Ingrese el inventario final deseado del 2do producto en el segundo semestre : "))
    total_unidades_2dop2dosem = produccion_unidades_2dop2dosem + inventario_final_deseado_2dop2dosem
    inventario_inicial_2dop2dosem = int(input("Ingrese el inventario inicial del 2do producto en el segundo semestre : "))
    unidades_requeridas_2dop2dosem = produccion_unidades_2dop2dosem + inventario_final_deseado_2dop2dorsem - inventario_inicial_2dop2dosem
    total_unidades_producir_2dop = unidades_requeridas_2dop1ersem + unidades_requeridas_2dop2dosem
    total_unidades_2dop = total_unidades_2dop1ersem + total_unidades_2dop2dosem
    
    #producto 3
    produccion_unidades_3erp1ersem = int(input("Ingrese la cantidad de unidades a producir del 3er producto en el primer semestre : "))
    inventario_final_deseado_3erp1ersem = int(input("Ingrese el inventario final deseado del 3er producto en el primer semestre : "))
    total_unidades_2dop1ersem = produccion_unidades_3erp1ersem + inventario_final_deseado_3erp1ersem
    inventario_inicial_3erp1ersem = int(input("Ingrese el inventario inicial del 3er producto en el primer semestre : "))
    unidades_requeridas_3erp1ersem = produccion_unidades_3erp1ersem + inventario_final_deseado_3erp1ersem - inventario_inicial_3erp1ersem
    
    produccion_unidades_3erp2dosem = int(input("Ingrese la cantidad de unidades a producir del 3er producto en el segundo semestre : "))
    inventario_final_deseado_3erp2dorsem = int(input("Ingrese el inventario final deseado del 3er producto en el segundo semestre : "))
    total_unidades_2dop1ersem = produccion_unidades_3erp2dosem + inventario_final_deseado_3erp2dosem
    inventario_inicial_3erp2dosem = int(input("Ingrese el inventario inicial del 3er producto en el segundo semestre : "))
    unidades_requeridas_3erp2dosem = produccion_unidades_3erp2dosem + inventario_final_deseado_3erp2dorsem - inventario_inicial_3erp2dosem
    total_unidades_producir_3erp = unidades_requeridas_3erp1ersem + unidades_requeridas_3erp2dosem
    total_unidades_3erp = total_unidades_3erp1ersem + total_unidades_3erp2dosem
    
    return total_unidades_producir_1erp, total_unidades_producir_2dop, total_unidades_producir_3erp

# Crear una lista de listas con los datos del presupuesto de requerimiento de materiales
datos_presupuesto_produccion= [
    ["PRODUCTO 1", "", "", ""],
    ["Unidades a vender", produccion_unidades_1erp1ersem, produccion_unidades_1erp2dosem , total_unidades_producir_1erp],
    ["Inventario Final", inventario_final_deseado_1erp1ersem , inventario_final_deseado_1erp2dorsem , inventario_final_deseado_1erp2dorsem],
    ["Total de unidades", total_unidades_1erp1ersem , total_unidades_1erp2dosem , total_unidades_1erp],
    ["Inventario Inicial", inventario_inicial_1erp1ersem , inventario_inicial_1erp2dosem , inventario_inicial_1erp2dosem],
    ["Unidades a Produccir", unidades_requeridas_1erp1ersem , unidades_requeridas_1erp2dosem , total_unidades_producir_1erp],
    
    ["PRODUCTO 2", "", "", ""],
    ["Unidades a vender", produccion_unidades_2dop1ersem, produccion_unidades_2dop2dosem , total_unidades_producir_2dop],
    ["Inventario Final", inventario_final_deseado_2dop1ersem , inventario_final_deseado_2dop2dorsem , inventario_final_deseado_2dop2dorsem],
    ["Total de unidades", total_unidades_2dop1ersem , total_unidades_2dop2dosem , total_unidades_2dop],
    ["Inventario Inicial", inventario_inicial_2dop1ersem , inventario_inicial_2dop2dosem , inventario_inicial_2dop2dosem],
    ["Unidades a Produccir", unidades_requeridas_2dop1ersem , unidades_requeridas_2dop2dosem , total_unidades_producir_2dop],
    
    ["PRODUCTO 3", "", "", ""],
    ["Unidades a vender", produccion_unidades_3erp1ersem, produccion_unidades_3erp2dosem , total_unidades_producir_3erp],
    ["Inventario Final", inventario_final_deseado_3erp1ersem , inventario_final_deseado_3erp2dorsem , inventario_final_deseado_3erp2dorsem],
    ["Total de unidades", total_unidades_3erp1ersem , total_unidades_3erp2dosem , total_unidades_3erp],
    ["Inventario Inicial", inventario_inicial_3erp1ersem , inventario_inicial_3erp2dosem , inventario_inicial_3erp2dosem],
    ["Unidades a Produccir", unidades_requeridas_3erp1ersem , unidades_requeridas_3erp2dosem , total_unidades_producir_3erp]
]

# Impresion de datos de presupuesto de requerimiento de materiales - Tabla 3
tabla = tabulate(datos_presupuesto_produccion, headers=["Producto", "1er. Semestre", "2do. Semestre", "Total Año"], tablefmt="grid")
# Mostrar la tabla
print("Presupuesto de Producción")
print(tabla)

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

# Tabla 7. Presupuesto de mano de obra directa
def presupuesto_mod_directa(mensaje):
  try:
    dato = float(input(mensaje))
    return dato
  except ValueError:
    print("Por favor, ingresa un número válido.")
    return presupuesto_mod_directa(mensaje)
  
# Pedir los datos necesarios del 1er. semestre para el presupuesto de mdo directa
print("\n1er SEMESTRE")
print("\nPRODUCTO 1")    
unidades_producir1_1 = float(input('Ingrese unidades a producir en el semestre 1: '))
horas_requeridas1_1 = float(input('Ingrese cantidad de horas requeridas por unidad del semestre 1: '))
cuota_por_hora1_1 = float(input('Ingrese la cantidad de la cuota por hora del semestre 1: '))
print("\nPRODUCTO 2")
unidades_producir2_1 = float(input('Ingrese unidades a producir en el semestre 1: '))
horas_requeridas2_1 = float(input('Ingrese cantidad de horas requeridas por unidad del semestre 1: '))
cuota_por_hora2_1 = float(input('Ingrese la cantidad de la cuota por hora del semestre 1: '))
print("\nPRODUCTO 3")    
unidades_producir3_1 = float(input('Ingrese unidades a producir en el semestre 1: '))
horas_requeridas3_1 = float(input('Ingrese cantidad de horas requeridas por unidad del semestre 1: '))
cuota_por_hora3_1 = float(input('Ingrese la cantidad de la cuota por hora del semestre 1: '))

# Calcular los valores del 1er. semestre para el presupuesto mdo directa
total_horas1_1 = unidades_producir1_1 * horas_requeridas1_1
total_horas2_1 = unidades_producir2_1 * horas_requeridas2_1
total_horas3_1 = unidades_producir3_1 * horas_requeridas3_1

importe_mod1_1 = total_horas1_1 * cuota_por_hora1_1
importe_mod2_1 = total_horas2_1 * cuota_por_hora2_1
importe_mod3_1 = total_horas3_1 * cuota_por_hora3_1

total_requeridas_sem1 = total_horas1_1 + total_horas2_1 + total_horas3_1

total_mod_sem1 = importe_mod1_1 + importe_mod2_1 + importe_mod3_1

# Pedir los datos necesarios del 2do. semestre para el presupuesto de mdo directa
print("\n2do SEMESTRE")
print("\nPRODUCTO 1")    
unidades_producir1_2 = float(input('Ingrese unidades a producir en el semestre 2: '))
horas_requeridas1_2 = float(input('Ingrese cantidad de horas requeridas por unidad del semestre 2: '))
cuota_por_hora1_2 = float(input('Ingrese la cantidad de la cuota por hora del semestre 2: '))
print("\nPRODUCTO 2")
unidades_producir2_2 = float(input('Ingrese unidades a producir en el semestre 2: '))
horas_requeridas2_2 = float(input('Ingrese cantidad de horas requeridas por unidad del semestre 2: '))
cuota_por_hora2_2 = float(input('Ingrese la cantidad de la cuota por hora del semestre 2: '))
print("\nPRODUCTO 3")    
unidades_producir3_2 = float(input('Ingrese unidades a producir en el semestre 2: '))
horas_requeridas3_2 = float(input('Ingrese cantidad de horas requeridas por unidad del semestre 2: '))
cuota_por_hora3_2 = float(input('Ingrese la cantidad de la cuota por hora del semestre 2: '))

# Calcular los valores del 2do. semestre para el presupuesto mod directa
total_horas1_2 = unidades_producir1_2 * horas_requeridas1_2
total_horas2_2 = unidades_producir2_2 * horas_requeridas2_2
total_horas3_2 = unidades_producir3_2 * horas_requeridas3_2

importe_mod1_2 = total_horas1_2 * cuota_por_hora1_2
importe_mod2_2 = total_horas2_2 * cuota_por_hora2_2
importe_mod3_2 = total_horas3_2 * cuota_por_hora3_2
total_requeridas_sem2 = total_horas1_2 + total_horas2_2 + total_horas3_2

total_mod_sem2 = importe_mod1_2 + importe_mod2_2 + importe_mod3_2

#Pedir los datos del año para el presupuesto de mod directa
print("\nAÑO")
print("\nPRODUCTO 1")    
unidades_producir1_3 = float(input('Ingrese unidades a producir en el semestre 3: '))
horas_requeridas1_3 = float(input('Ingrese cantidad de horas requeridas por unidad del semestre 1: '))
print("\nPRODUCTO 2")
unidades_producir2_3 = float(input('Ingrese unidades a producir en el semestre 3: '))
horas_requeridas2_3 = float(input('Ingrese cantidad de horas requeridas por unidad del semestre 1: '))
print("\nPRODUCTO 3")    
unidades_producir3_3 = float(input('Ingrese unidades a producir en el semestre 3: '))
horas_requeridas3_3 = float(input('Ingrese cantidad de horas requeridas por unidad del semestre 1: '))

# Calcular los valores del año para el presupuesto mod directa
total_horas1_3 = unidades_producir1_3 * horas_requeridas1_3
total_horas2_3 = unidades_producir2_3 * horas_requeridas2_3
total_horas3_3 = unidades_producir3_3 * horas_requeridas3_3

importe_mod1_3 = importe_mod1_1 + importe_mod1_2
importe_mod2_3 = importe_mod2_1 + importe_mod2_2
importe_mod3_3 = importe_mod3_1 + importe_mod3_2

total_requeridas_año = total_horas1_3 + total_horas2_3 + total_horas3_3
total_mod_año = importe_mod1_3 + importe_mod2_3 + importe_mod3_3

# Crear una lista de listas con los datos del presupuesto de mod directa
datos_presupuesto_mod_directa = [
    ["PRODUCTO 1", "", "", ""], 
    ["Unidades a producir", unidades_producir1_1, unidades_producir1_2, unidades_producir1_3], 
    ["Horas requeridas por unidad", horas_requeridas1_1, horas_requeridas1_2, horas_requeridas1_3], 
    ["Total de horas requeridas por unidad", total_horas1_1, total_horas1_2, total_horas1_3], 
    ["Cuota por hora", cuota_por_hora1_1, cuota_por_hora1_2, ""], 
    ["Importe de M.O.D", importe_mod1_1, importe_mod1_2, importe_mod1_3], 
    ["PRODUCTO 2", "", "", ""], 
    ["Unidades a producir", unidades_producir2_1, unidades_producir2_2, unidades_producir2_3], 
    ["Horas requeridas por unidad", horas_requeridas2_1, horas_requeridas2_2, horas_requeridas2_3], 
    ["Total de horas requeridas por unidad", total_horas2_1, total_horas2_2, total_horas2_3], 
    ["Cuota por hora", cuota_por_hora2_1, cuota_por_hora2_2, ""], 
    ["Importe de M.O.D", importe_mod2_1, importe_mod2_2, importe_mod2_3],
    ["PRODUCTO 3", "", "", ""], 
    ["Unidades a producir", unidades_producir3_1, unidades_producir3_2, unidades_producir3_3], 
    ["Horas requeridas por unidad", horas_requeridas3_1, horas_requeridas3_2, horas_requeridas3_3], 
    ["Total de horas requeridas por unidad", total_horas3_1, total_horas3_2, total_horas3_3], 
    ["Cuota por hora", cuota_por_hora3_1, cuota_por_hora3_2, ""], 
    ["Importe de M.O.D", importe_mod3_1, importe_mod3_2, importe_mod3_3], 
    ["Total de horas requeridas por semestre", total_requeridas_sem1, total_requeridas_sem2, total_requeridas_año], 
    ["Total de M.O.D por semestre", total_mod_sem1, total_mod_sem2, total_mod_año]
    ]

tabla = tabulate(datos_presupuesto_mod_directa, headers=["Producto", "1er. Semestre", "2do. Semestre", "Total Año"], tablefmt="grid")
    # Mostrar la tabla
print("Presupuesto de MOD directa")
print(tabla)

# Tabla 8. Presupuesto de gastos indirectos de fabricacion
def presupuesto_gastos_indirectos_fabricacion(mensaje):
  try:
    dato = float(input(mensaje))
    return dato
  except ValueError:
    print("Por favor, ingresa un número válido.")
    return presupuesto_gastos_indirectos_fabricacion(mensaje)

# Pedir los datos necesarios para el presupuesto de gastos indirectos de fabricacion
print("\n1er SEMESTRE")
depreciacion1= float(input('Ingrese monto de depreciacion: '))
seguros1 = float(input('Ingrese monto para seguros: '))
mantenimiento1 = float(input('Ingrese monto de mantenimiento: '))
energeticos1 = float(input('Ingrese monto de energeticos: '))
varios1 = float(input('Ingrese monto de varios: '))

# Calcular los valores del 1er. semestre para el presupuesto de gastos indirectos de fabricacion
total_gif1 = depreciacion1 + seguros1 + mantenimiento1 + energeticos1 + varios1

print("\n2do SEMESTRE")
depreciacion2 = float(input('Ingrese monto de depreciacion: '))
seguros2 = float(input('Ingrese monto para seguros: '))
mantenimiento2 = float(input('Ingrese monto de mantenimiento: '))
energeticos2 = float(input('Ingrese monto de energeticos: '))
varios2 = float(input('Ingrese monto de varios: '))

# Calcular los valores del 2do. semestre para el presupuesto de gastos indirectos de fabricacion
total_gif1 = depreciacion1 + seguros1 + mantenimiento1 + energeticos1 + varios1

print("\nAÑO")
depreciacion3 = float(input('Ingrese monto de depreciacion: '))
seguros3 = float(input('Ingrese monto para seguros: '))
mantenimiento3 = float(input('Ingrese monto de mantenimiento: '))
energeticos3 = float(input('Ingrese monto de energeticos: '))
varios3 = float(input('Ingrese monto de varios: '))

# Calcular los valores del año para el presupuesto de gastos indirectos de fabricacion
total_gif1 = depreciacion1 + seguros1 + mantenimiento1 + energeticos1 + varios1
total_gif2 = depreciacion2 + seguros2 + mantenimiento2 + energeticos2 + varios2
total_gif3 = depreciacion3 + seguros3 + mantenimiento3 + energeticos3 + varios3

# Coeficiente para determinar el costo por hora de Gastos Indirectos de Fabricacion 
total_gif_final = total_gif3

total_horas_mod_anual = float(input('Ingrese la cantidad del total horas M.O.D anual: '))

# Calcular los valores del costo por hora G.I.F
costo_hora_gif = total_gif_final / total_horas_mod_anual

# Crear una lista de listas con los datos del presupuesto de mod directa
datos_presupuesto_gastos_indirectos_fabricacion = [
  ["Depreciacion", depreciacion1, depreciacion2, depreciacion3], 
  ["Seguros", seguros1, seguros2, seguros3], 
  ["Mantenimiento", mantenimiento1, mantenimiento2, mantenimiento3], 
  ["Energeticos", energeticos1, energeticos2, energeticos3],  
  ["Varios", varios1, varios2, varios3], 
  ["Total G.I.F por semestre", total_gif1, total_gif2, total_gif3], 
  ["Coeficiente para determinar el costo por hora de Gastos Indirectos de Fabricacion", "", "", ""], 
  ["Total de G.I.F", total_gif1, total_gif2, total_gif3], 
  ["Total horas M.O.D Anual","", "", total_horas_mod_anual], 
  ["Costo por hora de G.I.F", "", "", costo_hora_gif]
]

tabla = tabulate(datos_presupuesto_gastos_indirectos_fabricacion, headers=["Producto", "1er. Semestre", "2do. Semestre", "Total Año"], tablefmt="grid")
    # Mostrar la tabla
print("Presupuesto de Gastos Indirectos de Fabricacion")
print(tabla)

# Tabla 9. Presupuesto de gastos de operacion
def presupuesto_gastos_operacion(mensaje):
  try:
    dato = float(input(mensaje))
    return dato
  except ValueError:
    print("Por favor, ingresa un número válido.")
    return presupuesto_gastos_operacion(mensaje)

# Pedir los datos necesarios para el presupuesto de gastos de operacion
print("\n1er SEMESTRE")
depreciacion1 = float(input('Ingrese monto de depreciacion del semestre 1: '))
sueldos_y_salarios1 = float(input('Ingrese monto de sueldos y salarios del semestre 1: '))
comisiones1 = float(input('Ingrese la cantidad del total de ventas del 1er semestre de su presupuesto de ventas: ')) 
varios1O = float(input('Ingrese monto de varios del semestre 1: '))
intereses_prestamo1 = float(input('Ingrese monto de intereses del prestamo del semestre 1: '))
print("\n2do SEMESTRE")
depreciacion2 = float(input('Ingrese monto de depreciacion del semestre 2: '))
sueldos_y_salarios2 = float(input('Ingrese monto de sueldos y salarios del semestre 2: '))
comisiones2 = float(input('Ingrese la cantidad del total de ventas del 2do semestre de su presupuesto de ventas: ')) * 0.01
varios2O = float(input('Ingrese monto de varios del semestre 2: '))
intereses_prestamo2 = float(input('Ingrese monto de intereses del prestamo del semestre 2: '))
print("\nAÑO")
depreciacion3 = float(input('Ingrese monto de depreciacion del semestre 3: '))
sueldos_y_salarios3 = float(input('Ingrese monto de sueldos y salarios del semestre 3: '))
comisiones3 = float(input('Ingrese la cantidad del total de ventas del año de su presupuesto de ventas: ')) * 0.01
varios3O = float(input('Ingrese monto de varios del semestre 3: '))
intereses_prestamo3 = float(input('Ingrese monto de intereses del prestamo del semestre 3: '))

# Calcular los valores para el presupuesto de gastos de operaciom
total_comisiones1 = comisiones1 * 0.01
total_comisiones2 = comisiones2 * 0.01
total_comisiones3 = comisiones3 * 0.01

total_gastos_operacion1 = depreciacion1 + sueldos_y_salarios1 + total_comisiones1 + varios1O + intereses_prestamo1
total_gastos_operacion2 = depreciacion2 + sueldos_y_salarios2 + total_comisiones2 + varios2O + intereses_prestamo2
total_gastos_operacion3 = depreciacion3 + sueldos_y_salarios3 + total_comisiones3 + varios3O + intereses_prestamo3

# Crear una lista de listas con los datos del presupuesto de mod directa
datos_presupuesto_gastos_operacion = [
  ["Depreciacion", depreciacion1, depreciacion2, depreciacion3], 
  ["Sueldos y salarios", sueldos_y_salarios1, sueldos_y_salarios2, sueldos_y_salarios3], 
  ["Comisiones", total_comisiones1, total_comisiones2, total_comisiones3], 
  ["Varios", varios1O, varios2O, varios3O], 
  ["Intereses del prestamo", intereses_prestamo1, intereses_prestamo2, intereses_prestamo3], 
  ["Total de Gastos de Operacion", total_gastos_operacion1, total_gastos_operacion2, total_gastos_operacion3]
]

tabla = tabulate(datos_presupuesto_gastos_operacion, headers=["Producto", "1er. Semestre", "2do. Semestre", "Total Año"], tablefmt="grid")
# Mostrar la tabla
print("Presupuesto de Gastos de Operacion")
print(tabla)
