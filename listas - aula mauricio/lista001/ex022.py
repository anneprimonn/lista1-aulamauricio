def maior_elemento(lista):
    return max(lista)

texto = input("Digite os números separados por espaço: ")

numeros_str = texto.split()

lista_numeros = []
for num in numeros_str:
    lista_numeros.append(float(num))
resultado = maior_elemento(lista_numeros)

if resultado is not None:
    print(f"O maior número da lista é: {resultado}")
