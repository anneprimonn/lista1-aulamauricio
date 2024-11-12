def conta_palavras(texto):
    palavras = texto.split()
    return len(palavras) 

texto_usuario = input("Digite um texto: ")
result = conta_palavras(texto_usuario)

print(f"O número de palavras no texto é: {result}")