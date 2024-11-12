def conta_letras(s, letra):
    return s.count(letra)

texto_usuario = input("Digite um testo: ")
letra_usuario = input("Digite a letra a ser contada: ")
result = conta_letras(texto_usuario, letra_usuario)

# Exibe o resultado
print(f"A letra '{letra_usuario}' aparece {result} vezes no texto.")
