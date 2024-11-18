def potencia(base, expoente):
    return base ** expoente
base_usuario = float(input('Digite a base:'))
expoente_usuario = float(input('Digite o expoente:'))
result = potencia(base_usuario,expoente_usuario)
print('R =',result)