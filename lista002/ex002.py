def produto_lista(lista):
    produto = 1
    for num in lista:
        produto *= num
    return produto
lista_usuario = (input('Digite a sua lista de números separados por espaço: '))
listas = [int(x) for x in lista_usuario.split()]
nova_lista = produto_lista(listas)
print(nova_lista)
