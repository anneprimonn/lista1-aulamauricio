def remove_duplicados(lista):
    # Usado o set() para eliminar duplicados e depois volta para a lista
    return list(set(lista))

lista_original = [1, 2, 3, 4, 5, 2, 3, 4, 6]
lista_sem_duplicados = remove_duplicados(lista_original)

print("Lista sem duplicados:", lista_sem_duplicados)
