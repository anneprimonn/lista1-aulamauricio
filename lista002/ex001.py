def multiplica_escalar(lista, escalar):
    resultado = []
    for x in lista:  
        r_conta = x * escalar  
        resultado.append(r_conta)  # adicionar um item
    return resultado 

lista_usuario = (input('Digite a sua lista de números separados por espaço: '))
listas = [int(x) for x in lista_usuario.split()] #split e int usado para converter para inteiros
escalar_usuario = int(input('Digite o escalar: '))
nova_lista = multiplica_escalar(listas,escalar_usuario)

print('Lista =',nova_lista)