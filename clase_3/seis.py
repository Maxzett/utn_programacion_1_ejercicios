'''
6 - Realizar un programa que: asigne a las variables numero1 y numero2 los valores
solicitados al usuario, valide los mismos entre 10 y 100, asigne a la variable operacion el
valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice la operación de dichos valores
a través de una función. Mostrar el resultado por pantalla.
'''

def sumar (a , b):
    return a + b

def restar (a , b):
    return a - b

while True:
    num_1 = int(input('Ingrese un numero: '))    
    num_2 = int(input('Ingrese un numero: '))    

    operacion = input('Elija la opereacion (s - sumar, r - restar)')
    while operacion != 's' and operacion != 'r':
            operacion = input('Elija nuevamente la opereacion (s - sumar, r - restar)')        

    if operacion == 'r':
        print(f'El resultado de la resta es: {restar(num_1, num_2)}')
        break
    else:
        print(f'El resultado de la suma es: {sumar(num_1, num_2)}')
        break
    
