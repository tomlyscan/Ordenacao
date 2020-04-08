import numpy as np

def find_min(arr):
    min = arr[0]
    index = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            index = i
    return index

def selection_sort(arr):
    cpy = arr[1:]                       # cria uma copia da entrada
    ord = []
    for i in range(len(cpy)):
        index = find_min(cpy)           # retorna o indice do menor valor da lista
        ord.append(cpy[index])          # copia o menor valor para a lista ordenada
        cpy = np.delete(cpy, index)     # deleta o menor valor atual
    return ord

def insertion_sort(arr):
    cpy = arr[1:]
    for i in range(1, len(cpy)):
        for j in range(i, 0, -1):
            if cpy[j] < cpy[j-1]:
                a = cpy[j-1]
                cpy[j-1] = cpy[j]
                cpy[j] = a
    return cpy