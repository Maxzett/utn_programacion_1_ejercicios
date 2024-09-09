'''
Ejercicio 8:
Genere un segundo módulo en el cual existan las funciones necesarias para la gestión del
equipo de recursos humanos de la empresa.
En el mismo debe existir una primera función que calcule el valor del salario de cada
empleado. El valor del mismo es la cantidad de horas trabajadas multiplicadas por 10 y un
incremento del 3% por cada año de antigüedad.
También debe haber una segunda función que calcule la productividad del empleado. La
misma se calcula como la cantidad de artefactos producidos, dividido por la cantidad de
horas de trabajo.
En tercer lugar debe haber una función que reporte toda la información del empleado
incluyendo la calculada en las dos funciones anteriores, nombre y edad.
'''

def calcular_salario(horas_trabajadas, antiguedad ):
    salario_parcial = horas_trabajadas * 10
    incremento = salario_parcial * (0.03 * antiguedad)
    salario_final = salario_parcial + incremento    
    return salario_final

def calcular_productividad(cant_producuccion, horas_trabajadas):
    if cant_producuccion == 0:
        return 0
    productividad = cant_producuccion / horas_trabajadas
    return productividad    

def reportar_empleado(datos_empleado):
    
    nombre, edad, horas_trabajadas, antiguedad, cant_produccion = datos_empleado
    salario = calcular_salario(horas_trabajadas, antiguedad)
    productividad = calcular_productividad(cant_produccion, horas_trabajadas)

    reporte = f"""
    Info del empleado:
    Nombre: {nombre}
    Edad: {edad}
    Horas trabajadas: {horas_trabajadas}
    Antiguedad: {antiguedad} años
    Artefactos producidos: {cant_produccion}
    Salario: {salario:.2f} 
    Productividad: {productividad:.2f} artefactos por hora
    """
    return reporte