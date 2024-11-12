def conta_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    for v in texto:
        if v in vogais:
            contador += 1  
    return contador

texto_usuario = input("Digite um texto: ")
result = conta_vogais(texto_usuario)

print(f"O número de vogais no texto é: {result}")