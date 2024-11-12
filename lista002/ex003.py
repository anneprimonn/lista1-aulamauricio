def conta_consoantes(texto):
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    contador = 0
    for c in texto:
        if c in consoantes:
            contador += 1  
    return contador

texto_usuario = input("Digite um texto: ")
result = conta_consoantes(texto_usuario)

print(f"O número de consoantes no texto é: {result}")