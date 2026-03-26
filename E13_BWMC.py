#BWMC
SALARIO_BASE = 3500.00
BONO_PRODUCTIVIDAD = 500.00
IMPUESTO = 0.12


# Datos del empleado (variables)
nombre_empleado = "Brandon Martinez"
es_empleado_fijo = True

# Calculo del salario bruto (salario base + bono)
salario_bruto = SALARIO_BASE + BONO_PRODUCTIVIDAD

# Cálculo del descuento por impuestos
descuento = salario_bruto * IMPUESTO

# Cálculo del salario neto
salario_neto = salario_bruto - descuento

# Mostrar información
print("Nombre del empleado:", nombre_empleado)
print("¿Empleado fijo ?: ", es_empleado_fijo)
print("Salario base:", SALARIO_BASE)
print("Bono de productividad:", BONO_PRODUCTIVIDAD)
print("Salario bruto:", salario_bruto)
print("Descuento por impuesto:", descuento)
print("Salario neto:", salario_neto)