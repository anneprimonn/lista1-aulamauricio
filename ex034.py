def hipotenusa(a, b):
    return (a ** 2 + b **2) ** 0.5
a_usuario = float(input('Digite o valor de A:'))
b_usuario = float(input('Digite o valor de B:'))
result = hipotenusa(a_usuario,b_usuario)
print('R =',result)