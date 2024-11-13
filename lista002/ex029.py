def intervalo_entre_elementos(lista):
    maior = max(lista) 
    menor = min(lista)  
    intervalo = maior - menor  
    return intervalo

lista_usuario = input('Digite uma lista de números (separados por espaço): ').split()
lista_usuario = [int(x) for x in lista_usuario]  
resultado = intervalo_entre_elementos(lista_usuario)

if resultado is None:
    print("A lista está vazia. Não é possível calcular o intervalo.")
else:
    print(f'O intervalo entre o maior e o menor valor da lista é: {resultado}')
