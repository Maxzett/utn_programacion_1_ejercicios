'''
Ejercicio 7:
Supongamos que le solicito a chatgpt una función para calcular valores de ventas de
productos con impuestos para una determinada empresa:
La respuesta de chatgpt es:
def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones = 15):
resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
resultado_final = resultado_nacional + resultado_exportaciones
return resultado_final
¿Considera que cumple con los objetivos de una función?
Corrija la función dentro de un módulo, divida en distintas funciones de ser necesario,
documente y denomine correctamente.
'''

def calcular_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones = 15):
    resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
    resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
    resultado_final = resultado_nacional + resultado_exportaciones
    return resultado_final

print(calcular_impuestos(1200, 1000))