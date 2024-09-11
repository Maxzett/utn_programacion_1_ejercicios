'''
5 - Realizar un programa que: asigne a la variable numero1 un valor solicitado al usuario,
valide el mismo entre 10 y 100, realice un descuento del 5% a dicho valor a través de una
función llamada realizarDescuento(). Mostrar el resultado por pantalla. Atención: pueden
reutilizarse funciones ya creadas.
'''

def realizar_descuento(num:int):
    descuento = 0.05
    resultado = num * descuento
    numero_con_descuento = num - resultado
    return numero_con_descuento 

while True:
    numero_1 = int(input('Ingrese un numero del 10 al 100: '))
    if numero_1 >= 10 and numero_1 <= 100:
        break

print(realizar_descuento(numero_1))

