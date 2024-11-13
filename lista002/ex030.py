def histograma(lista):
    ocorrencias = {}
    for elementos in lista:
        if elementos in ocorrencias:
            ocorrencias[elementos] += 1
        else:
            ocorrencias[elementos] = 1
    return ocorrencias

lista_usuario = input('Digite uma lista de números (separados por espaço): ').split()
lista_usuario = [int(x) for x in lista_usuario] 
resultado = histograma(lista_usuario)

print("Histograma de ocorrências:", resultado)