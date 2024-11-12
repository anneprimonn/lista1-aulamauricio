def soma_naturais(n):
    soma = 0
    for i in range(n):  # De 0 até n-1
        soma += i
    return soma

n = int(input('Digite o valor de n para calcular a soma dos N primeiros números naturais: '))
soma_final = soma_naturais(n)

print(f'A soma dos {n} primeiros números naturais é: {soma_final}')
