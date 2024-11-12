def capitaliza_palavras(texto):
    return texto.capitalize()

texto_usuario = input("Digite um texto: ")
resultado = capitaliza_palavras(texto_usuario)

print(f"O texto com as palavras capitalizadas é: {resultado}")
