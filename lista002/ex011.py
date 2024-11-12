def produto_escalar(vetor1, vetor2):
    if len(vetor1) != len(vetor2):
        return "devem ter o mesmo tamanho."
    produto = 0
    for i in range(len(vetor1)):
        produto += vetor1[i] * vetor2[i]
    return produto

vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
resultado = produto_escalar(vetor1, vetor2)

print(f"O produto escalar entre os vetores é: {resultado}")
