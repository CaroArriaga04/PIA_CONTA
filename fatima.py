##AQUI VOY YOOO FATIMAAA!!!

#Tabla 12 Estado de Costo de Producción y Ventas:
def estado_costo_ventas(mensaje):
  try:
    dato = float(input(mensaje))
    return dato
  except ValueError:
    print("Por favor, ingresa un número válido.")
    return estado_costo_ventas(mensaje)


saldo_ini_materiales= float(input("\nIngresa el saldo inicial de los materiales: "))
compras_materiales = com_total_1 + com_total_2
material_disponible = saldo_ini_materiales + compras_materiales
invent_final = (costo_unitario_ta+costo_unitario_tb+costo_unitario_tc)
materiales_utilizados= material_disponible - invent_final
mano_obra_directa= total_mod_sem1 + total_mod_sem2
total_gif_final = total_gif3
costo_produccion= materiales_utilizados + mano_obra_directa + total_gif_final
invent_inicial = input("Ingresa el inventario inicial de productos terminados: ")
total_produccion_dispo= costo_produccion + invent_inicial
total_de_costos=(costo_unitario_t1+costo_unitario_t2+costo_unitario_t3)
costo_ventas= total_produccion_dispo - total_de_costos


# Crear una lista de listas 
datos_destado_costo_produccion_ventas= [
    ["\nEstado de costo de producción y ventas"],
    ["Saldo inicial de los materiales: ", saldo_ini_materiales],
    ["Compras de materiales",compras_materiales],
    ["Material disponible",material_disponible]
    ["Inventario final de materiales",invent_final]
    ["Materiales utilizados",materiales_utilizados]
    ["Mano de obra directa",mano_obra_directa],
    ["Gastos de fabricación indirectos",total_gif_final],
    ["Costo de producción",costo_produccion],
    ["Inventario inicial de productos terminados",invent_inicial],
    ["Total de producción disponible",total_produccion_dispo],
    ["Inventario final de prioductos terminados",total_de_costos]
    ["Costo de ventas",costo_ventas],
]

#print(tabulate(total_costo_unitario1, headers=["", "", "", ""], tablefmt="fancy_grid"))


#Tabla 13 Estado de resultados
def estado_resultados (mensaje):
  try:
    dato = float(input(mensaje))
    return dato
  except ValueError:
    print("Por favor, ingresa un número válido.")
    return inventarios_finales(mensaje)

total_ventas_año = total_ventas_1sem + total_ventas_2sem 
costo_ventas= total_produccion_dispo - total_de_costos
utilidad_bruta=input("Ingrese la utilidad bruta: ")
gastos_operacion= total_gastos_operacion1 + total_gastos_operacion2 
utilidad_operacion= utilidad_bruta - gastos_operacion
isr=input("Ingresa el ISR: ")
ptu=input("Ingresa el PTU: ")
utilidad_neta= utilidad_operacion - isr - ptu

estado_de_resultados=[
    ["\nEstado de resultados"]
    ["Ventas: ", total_ventas_año],
    ["Costo de ventas: ",costo_ventas],
    ["Utilidad bruta: ",utilidad_bruta],
    ["Gastos de operación: ",gastos_operacion],
    ["Utilidad de operación: ",utilidad_operacion],
    ["ISR",isr],
    ["PTU",ptu],
    ["Utilidad neta",utilidad_neta],
]


#Tabla 14 Estado de flujo de efectivo
def estado_flujo_efectivo(mensaje):
  try:
    dato = float(input(mensaje))
    return dato
  except ValueError:
    print("Por favor, ingresa un número válido.")
    return inventarios_finales(mensaje)

saldo_inicial=int(input("Ingresa el saldo inicial: "))
por_cobranza_2022
por_cobranza_2023
total_entrada= por_cobranza_2022 + por_cobranza_2023
efectivo_dispo= saldo_inicial + por_cobranza_2022 + por_cobranza_2023
saldo_proveedores_31_dic_año
por_proveedor_año1
pago_mano_obra= total_mod_sem1, total_mod_sem2, total_mod_año
gastos_indirectos= total_gif1 + total_gif2 + total_gif3
depreciacion= depreciacion1 + depreciacion2 + depreciacion3
gastos_indirectos_fabricacion=gastos_indirectos - depreciacion
total_gastos= total_gastos_operacion1 + total_gastos_operacion2 + total_gastos_operacion3
depre=depreciacion1 + depreciacion2 + depreciacion3
gastos_operacion= total_gastos - depre
activo_fijo=int(input("Ingresa el activo fijo: "))
isr2=int(input("Ingresa el ISR de la redaccion: "))
isr
total_salidas=saldo_proveedores_31_dic_año + por_proveedor_año1 + pago_mano_obra + gastos_indirectos_fabricacion + gastos_operacion + activo_fijo + isr2 + isr 



estado_de_flujo_efectivo=[
    ["\nEstado de flujo efectivo"],
    ["Saldo inicial de efectivo",saldo_inicial],
    ["Entradas:"],
    ["Cobranza del 2022", por_cobranza_2022],
    ["Cobranza del 2023", por_cobranza_2023],
    ["Total de entradas",total_entrada],
    ["Efectivo disponible",efectivo_dispo], 
    ["Salidas:"],
    ["Proveedores 2023", saldo_proveedores_31_dic_año],
    ["Proveedores 2022",por_proveedor_año1],
    ["Pago mano de obra directa", pago_mano_obra],
    ["Pago gastos indirectos de fabricación", gastos_indirectos_fabricacion],
    ["Pago de gastos de operación", gastos_operacion],
    ["Compra de activo fijo (maquinaria)",activo_fijo],
    ["Pago ISR 2022", isr2],
    ["Pago ISR 2023",isr]
    ["Total de salidas", total_salidas],
    ["Flujo de efectivo actual", ],  #PENDIENTE
]


#Tabla 15

