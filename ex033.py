def area_circulo(raio):
    pi = 3.14
    return pi * raio ** 2
area_usuario = float(input('Digite a area:'))
result = area_circulo(area_usuario)
print('R =',result)