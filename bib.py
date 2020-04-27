import numpy as np
import math

def find_min(arr):
    min = arr[0]
    index = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            index = i
    return index

def selection_sort(arr):
    A = arr                       # cria uma copia da entrada
    ord = []
    for i in range(len(A)):
        index = find_min(A)           # retorna o indice do menor valor da lista
        ord.append(A[index])          # copia o menor valor para a lista ordenada
        A = np.delete(A, index)     # deleta o menor valor atual
    return ord

def insertion_sort(arr):
    A = arr
    for i in range(1, len(A)):
        for j in range(i, 0, -1):
            if A[j] < A[j-1]:
                a = A[j-1]
                A[j-1] = A[j]
                A[j] = a
    return A

def merge(A, L, R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
        
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
        
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

def merge_sort(A):  
    if len(A) > 1:
        q = len(A)//2            # Divisao inteira
        L = A[:q]
        R = A[q:]       
        
        merge_sort(L)
        merge_sort(R)
        merge(A, L, R)
    return A



def quick_sort(arr):
    pass