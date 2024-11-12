def retira_espacos(texto):
    return texto.replace(" ", "")

texto_usuario = input("Digite um texto: ")
result = retira_espacos(texto_usuario)

# Exibe o resultado
print(f"O texto sem espaços em branco é: {result}")
