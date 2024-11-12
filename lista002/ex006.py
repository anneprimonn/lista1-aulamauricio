def diferenca_conjuntos(lista1, lista2):
    # Converter as listas para conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    #conjunto1 que não esta no conjunto2)
    diferenca = conjunto1 - conjunto2
    return list(diferenca)

lista1_usuario = input('Digite a primeira lista de números (separados por espaço): ').split()
lista2_usuario = input('Digite a segunda lista de números (separados por espaço): ').split()
lista1_usuario = [int(x) for x in lista1_usuario]
lista2_usuario = [int(x) for x in lista2_usuario]
resultado = diferenca_conjuntos(lista1_usuario, lista2_usuario)

print(f'A diferença entre as duas listas é: {resultado}')
