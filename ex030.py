def uniao_listas(lista1, lista2):
    lista_unida = lista1 +  lista2
    return lista_unida

lista1_usuario = input('Digite a primeira lista(separados por espaço): ')
lista_numeros = [float(num) for num in lista1_usuario.split()]
lista2_usuario = input('Digite a primeira lista(separados por espaço): ')
lista_numeros = [float(num) for num in lista2_usuario.split()]
result = uniao_listas(lista1_usuario,lista2_usuario)

print('A lista unida:',result)