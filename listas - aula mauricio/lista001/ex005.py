def mult_tres_numeros(a, b, c):
    mult = a * b * c
    return mult 

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
result = mult_tres_numeros(n1, n2, n3)

print("R =", result)
