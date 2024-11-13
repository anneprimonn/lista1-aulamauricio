def remove_multiplos(lista, n):
    nova_lista =[]
    for x in lista: 
        if x % n != 0: 
            nova_lista.append(x) 
    return nova_lista

lista_usuario = input('Digite a primeira lista de números (separados por espaço): ').split()
multi_usuario = int(input('Digite um valor de multiplos: '))
lista_usuario = [int(n) for n in lista_usuario]
result =remove_multiplos(lista_usuario,multi_usuario)

print('Lista original: ',lista_usuario)
print(f'Lista sem mutilplos de {multi_usuario}: {result} ')