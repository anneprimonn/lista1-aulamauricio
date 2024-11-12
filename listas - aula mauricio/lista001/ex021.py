def media_lista(lista):
    soma = sum(lista)
    media = soma / len(lista) #numero de elemnetos
    return media

texto = input("Digite os números separados por espaço: ")
lista_numeros = [float(num) for num in texto.split()]
result = media_lista(lista_numeros)

print(f"A média dos números é: {result}")
