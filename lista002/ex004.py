def concatena_listas(lista1, lista2):
    n_lista = lista1 + lista2
    return n_lista
lista1_usuario = input("Digite os elementos da primeira lista (separados por espaço): ").split()
lista2_usuario = input("Digite os elementos da segunda lista (separados por espaço): ").split()
lista1_usuario = [int(x) for x in lista1_usuario]
lista2_usuario = [int(x) for x in lista2_usuario]
concatenado = concatena_listas(lista1_usuario,lista2_usuario)
print(concatenado)
         