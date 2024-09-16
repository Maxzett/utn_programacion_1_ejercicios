'''
Repaso funciones
1- Elabore un módulo que contenga 3 funciones:
a- una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
que en caso de no recibir un radio el valor del mismo será 3.
b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
parámetro, sin parámetros opcionales.
c- una función que calcule el área de un triángulo recibiendo base y altura por parámetro.
2- Elaborar un módulo que contenga 3 funciones. Pero este deberá calcular los perímetros
de las mismas figuras que el punto 1.
3- generar paquete.
4- subir a github.
'''

from package.modulo_areas import * 
from package.modulo_perimetros import *

#vamos a llamar a las funciones del modulo areas
radio = 3
print(f'El area de un circulo de radio {radio}, es de {calcular_area_circulo(radio):.2f}')

long_lado = 4
print(f'El area de un cuadrado con los lados de {long_lado} es de {calcular_area_cuadrado(long_lado)}')

base = 5
altura = 4
print(f'El area de un triangulo de base {base} y de una altura de {altura} es de {calcular_area_triangulo(base,altura)}')

#a continuacion llamamos a las funciones del modulo perimetros

radio2 = 5
print(f'El perimetro de un circulo de radio {radio2}, es de {calcular_per_circulo(radio2):.2f}')

lado2 = 6
print(f'El perimetro de un cuadrado con lados de {lado2}, es de {calcular_per_cuadrado(lado2)}')

l1 = 3
l2 = 5
l3 = 3
print(f'El perimetro de un triangulo con lados de {l1, l2, l3}, es de {calcular_per_triangulo(l1,l2,l3)}')