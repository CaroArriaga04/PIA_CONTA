from tabulate import tabulate

def presupuesto_produccion(mensaje):
  try:
    dato = float(input(mensaje))
    return dato
  except ValueError:
    print("Por favor, ingresa un número válido.")
    return presupuesto_produccion(mensaje)
  
print("\nPRODUCTO 1")
produccion_unidades_1erp1ersem = int(input("Ingrese la cantidad de unidades a producir del 1er producto en el primer semestre : "))
inventario_final_deseado_1erp1ersem = int(input("Ingrese el inventario final deseado del 1er producto en el primer semestre : "))
total_unidades_1erp1ersem = produccion_unidades_1erp1ersem + inventario_final_deseado_1erp1ersem
inventario_inicial_1erp1ersem = int(input("Ingrese el inventario inicial del 1er producto en el primer semestre : "))
unidades_requeridas_1erp1ersem = produccion_unidades_1erp1ersem + inventario_final_deseado_1erp1ersem - inventario_inicial_1erp1ersem

produccion_unidades_1erp2dosem = int(input("Ingrese la cantidad de unidades a producir del 1er producto en el segundo semestre : "))
inventario_final_deseado_1erp2dosem = int(input("Ingrese el inventario final deseado del 1er producto en el segundo semestre : "))
total_unidades_1erp2dosem = produccion_unidades_1erp2dosem + inventario_final_deseado_1erp2dosem
inventario_inicial_1erp2dosem = int(input("Ingrese el inventario inicial del 1er producto en el segundo semestre : "))

unidades_requeridas_1erp2dosem = produccion_unidades_1erp2dosem + inventario_final_deseado_1erp2dosem - inventario_inicial_1erp2dosem
total_unidades_producir_1erp = unidades_requeridas_1erp1ersem + inventario_inicial_1erp2dosem
total_unidades_1erp = total_unidades_producir_1erp + inventario_final_deseado_1erp2dosem

print("\nPRODUCTO 2")
produccion_unidades_2dop1ersem = int(input("Ingrese la cantidad de unidades a producir del 2do producto en el primer semestre : "))
inventario_final_deseado_2dop1ersem = int(input("Ingrese el inventario final deseado del 2do producto en el primer semestre : "))
total_unidades_2dop1ersem = produccion_unidades_2dop1ersem + inventario_final_deseado_2dop1ersem
inventario_inicial_2dop1ersem = int(input("Ingrese el inventario inicial del 2do producto en el primer semestre : "))
unidades_requeridas_2dop1ersem = produccion_unidades_2dop1ersem + inventario_final_deseado_2dop1ersem - inventario_inicial_2dop1ersem

produccion_unidades_2dop2dosem = int(input("Ingrese la cantidad de unidades a producir del 2do producto en el segundo semestre : "))
inventario_final_deseado_2dop2dorsem = int(input("Ingrese el inventario final deseado del 2do producto en el segundo semestre : "))
total_unidades_2dop2dosem = produccion_unidades_2dop2dosem + inventario_final_deseado_2dop2dorsem
inventario_inicial_2dop2dosem = int(input("Ingrese el inventario inicial del 2do producto en el segundo semestre : "))
unidades_requeridas_2dop2dosem = produccion_unidades_2dop2dosem + inventario_final_deseado_2dop2dorsem - inventario_inicial_2dop2dosem
total_unidades_producir_2dop = unidades_requeridas_2dop1ersem + unidades_requeridas_2dop2dosem
total_unidades_2dop = total_unidades_2dop1ersem + total_unidades_2dop2dosem

print("\nPRODUCTO 3")
produccion_unidades_3erp1ersem = int(input("Ingrese la cantidad de unidades a producir del 3er producto en el primer semestre : "))
inventario_final_deseado_3erp1ersem = int(input("Ingrese el inventario final deseado del 3er producto en el primer semestre : "))
total_unidades_3erp1ersem = produccion_unidades_3erp1ersem + inventario_final_deseado_3erp1ersem
inventario_inicial_3erp1ersem = int(input("Ingrese el inventario inicial del 3er producto en el primer semestre : "))
unidades_requeridas_3erp1ersem = produccion_unidades_3erp1ersem + inventario_final_deseado_3erp1ersem - inventario_inicial_3erp1ersem

produccion_unidades_3erp2dosem = int(input("Ingrese la cantidad de unidades a producir del 3er producto en el segundo semestre : "))
inventario_final_deseado_3erp2dorsem = int(input("Ingrese el inventario final deseado del 3er producto en el segundo semestre : "))
total_unidades_3erp2dosem = produccion_unidades_3erp2dosem + inventario_final_deseado_3erp2dorsem
inventario_inicial_3erp2dosem = int(input("Ingrese el inventario inicial del 3er producto en el segundo semestre : "))
unidades_requeridas_3erp2dosem = produccion_unidades_3erp2dosem + inventario_final_deseado_3erp2dorsem - inventario_inicial_3erp2dosem
total_unidades_producir_3erp = unidades_requeridas_3erp1ersem + unidades_requeridas_3erp2dosem
total_unidades_3erp = total_unidades_3erp1ersem + total_unidades_3erp2dosem


# Crear una lista de listas con los datos del presupuesto de requerimiento de materiales
datos_presupuesto_produccion= [
    ["PRODUCTO 1", "", "", ""],
    ["Unidades a vender", produccion_unidades_1erp1ersem, produccion_unidades_1erp2dosem , total_unidades_producir_1erp],
    ["Inventario Final", inventario_final_deseado_1erp1ersem , inventario_final_deseado_1erp2dosem , inventario_final_deseado_1erp2dosem],
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
tabla = tabulate(datos_presupuesto_produccion, headers=["Producto", "1er. Semestre", "2do. Semestre", "Total Año"], tablefmt="fancy_grid")
# Mostrar la tabla
print("Presupuesto de Producción")
print(tabla)