def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:  
            soma += num   
    return soma

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = soma_pares(lista_numeros)

print("A soma dos números pares é:", result)
