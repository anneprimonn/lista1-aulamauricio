def conta_intervalo(lista, inicio, fim):
    contador = 0
    for n in lista:
        if inicio <= n <= fim:
            contador += 1
    return contador
    
lista1_usuario = input('Digite a primeira lista de números (separados por espaço): ').split()
lista1_usuario = [int(x) for x in lista1_usuario] # transforma para int
inicio_usuario = int(input('Digite o inicio: '))
fim_usuario = int(input('Digite o fim: '))
resultado = conta_intervalo(lista1_usuario, inicio_usuario, fim_usuario)

print(f'Quantidade de números dentro do intervalo [{inicio_usuario}, {fim_usuario}]: {resultado}')