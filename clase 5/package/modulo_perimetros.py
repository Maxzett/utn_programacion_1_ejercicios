'''
2- Elaborar un módulo que contenga 3 funciones. Pero este deberá calcular los perímetros
de las mismas figuras que el punto 1.'''

def calcular_per_circulo(radio):
    '''calculamos el perimetro de un circulo
    pasamos por parametro el radio
    nos devuelve el perimetro
    '''
    pi = 3.14
    perimetro = 2 * pi * radio 
    return perimetro


def calcular_per_cuadrado(lado):
    '''se pasa un lado del cuadrado
    se multiplica por 4
    retorna el perimetro
    '''
    perimetro = lado * 4
    return perimetro    


def calcular_per_triangulo(l1, l2, l3):
    '''calculamos en el perimetro de un triangulo
    pasando por parametro sus tres lado
    la suma de estos, nos devuelve su perimetro
    '''
    perimetro = l1 + l2 + l3
    return perimetro

