def eh_par(numero):
    if numero % 2 == 0: 
        return True
    else:
        return False

n1 = int(input("Digite um número: "))
result = eh_par(n1)

print("É par?", result)
