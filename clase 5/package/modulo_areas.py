'''a- una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
que en caso de no recibir un radio el valor del mismo será 3.'''

def calcular_area_circulo(radio = 3) -> float:
    pi = 3.14
    area = pi * (radio ** 2)
    return area

'''
b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
parámetro, sin parámetros opcionales.'''

def calcular_area_cuadrado(long_lado) -> float:
    area = long_lado * long_lado
    return area


'''c- una función que calcule el área de un triángulo recibiendo base y altura por parámetro.
'''

def calcular_area_triangulo(base, altura) -> float:
    area = 0.5 * base * altura
    return area

    