def multiplica_pares(lista):
    resultado = 1 
    for n in lista:    
        if n % 2 == 0:
            resultado *= n
    return resultado
lista_usuario = input('Digite a primeira lista de números (separados por espaço): ').split()
lista_usuario = [int(n) for n in lista_usuario]
result = multiplica_pares(lista_usuario)
print('A multiplicação dos numeros impares são',result)