'''2 - Resolver mediante recursividad el problema de las torres de Hanoi'''

def hanoi(discos: int, inicio, destino, aux):
    if  discos == 1:
        print(f'Mueve el disco 1 de {inicio} a {destino}')
        return
    else:
        hanoi( discos - 1, inicio, aux , destino)
        print(f'Mueve el disco {discos} de {inicio} a {destino}')
        hanoi(discos - 1, aux, destino, inicio)


hanoi(3, "Torre Inicio", "Torre Destino", "Torre Auxiliar")
