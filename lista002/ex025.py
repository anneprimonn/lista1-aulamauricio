def concatena_strings(lista_strings):
    #join para concatenar todas as strings da lista
    return ''.join(lista_strings)

lista = input('Digite uma lista de strings (separadas por espaço): ').split()
resultado = concatena_strings(lista)
print(f'Resultado da concatenação: {resultado}')
