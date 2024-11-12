def encontra_palavra(texto, palavra):
    
    return texto.find(palavra)

texto_usuario = input("Digite um texto: ")
palavra_usuario = input("Digite a palavra a ser encontrada: ")
indice = encontra_palavra(texto_usuario, palavra_usuario)

if indice != -1:
    print(f"A palavra '{palavra_usuario}' foi encontrada no índice {indice}.")
else:
    print(f"A palavra '{palavra_usuario}' não foi encontrada no texto.")
