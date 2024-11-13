def esta_ordenada(lista):
    for n in range(len(lista) - 1):
        if lista[n] > lista[n + 1]: 
            return False
    return True  
lista_usuario = input('Digite a primeira lista de números (separados por espaço): ').split()
lista_usuario = [int(n) for n in lista_usuario]
result = esta_ordenada(lista_usuario)
print(result)