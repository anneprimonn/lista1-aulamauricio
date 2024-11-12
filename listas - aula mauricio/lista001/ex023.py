def maior_elemento(lista):
    return min(lista)

texto = input("Digite os números separados por espaço: ")

numeros_str = texto.split()

lista_numeros = []
for num in numeros_str:
    lista_numeros.append(float(num))
result = maior_elemento(lista_numeros)

if result is not None:
    print(f"O menor número da lista é: {result}")


