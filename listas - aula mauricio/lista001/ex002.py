def maior(a, b):
    if a > b:
        return a
    else:
        return b

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

result = maior(n1, n2)

print("O maior número é:", result)
