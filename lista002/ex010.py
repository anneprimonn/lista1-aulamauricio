def diferenca_max_min(lista):
    maior = max(lista)
    menor = min(lista)
    return maior - menor #diferencça

lista_usuario = [64, 25, 12, 22, 11]
resultado = diferenca_max_min(lista_usuario)

print(f"A diferença entre o maior e o menor valor é: {resultado}")
