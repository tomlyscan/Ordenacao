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

def partition(arr,low,high): 
    i = ( low-1 )         
    pivot = arr[high]     
  
    for j in range(low , high): 
        if   arr[j] <= pivot: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
   
def quickSort(arr,low,high): 
    if low < high: 
  
        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
    return arr

def counting_sort(a):
    ordenada = []
    contador = max(a) + abs(min(a)) + 1
    pos_zero = abs(min(a))
    lista_contador = [0]*contador
    for i in range(len(a)):
        if a[i] == 0:
            lista_contador[pos_zero] += 1
        else:
            lista_contador[pos_zero + a[i]] += 1
    for i in range(len(lista_contador)):
        if lista_contador[i] > 0:
            for j in range(lista_contador[i]):
                if i == pos_zero:
                    ordenada += [0]
                else:
                    ordenada += [i - pos_zero]
    return ordenada

def number_to_list(num):
    negative = False
    res = []
    for x in str(num):
        if x == '-':
            negative = True
            continue
        if negative == True:
            res += [int(x)*-1]
            negative = False
            continue
        res += [int(x)]
    return res

def largest_digit_number(a):
    menor = abs(min(a))
    maior = abs(max(a))
    digitos_menor = int(math.log10(menor)) +1
    digitos_maior = int(math.log10(maior)) +1
    return digitos_maior if digitos_maior > digitos_menor else digitos_menor

def list_to_row(num, largest_digit_number, index=1 ):
    list = number_to_list(num)
    for x in range(0, (largest_digit_number+1) - len(list)):
        list = [0] + list
    list[0] = index
    return list

def list_to_matrix(a):
    matrix = []
    largest = largest_digit_number(a)
    for i in range(len(a)):
        matrix += [list_to_row(a[i], largest, i )]
    return matrix

def sorted_matrix(a):
    arr2D = np.array(list_to_matrix(a))
    for i in range(1, largest_digit_number(a)+1):
        arr2D = arr2D[arr2D[:, -i].argsort()]
    return arr2D

def radix_sort(a):
    sorted_list = []
    radix_matrix = sorted_matrix(a)
    for i in range(len(radix_matrix)):
        sorted_list += [a[radix_matrix[i][0]]]
    return sorted_list

def bucket_sort(a):
    bucket_length = 10
    bucket_positive = [[]]*bucket_length
    bucket_negative = [[]]*bucket_length
    ldn = largest_digit_number(a)
    num = 0.0
    res = []
    for i in range(len(a)):
        num = a[i]/math.pow(bucket_length,ldn-1)
        if num < 0:
            if not bucket_negative[int(abs(num))]:
                bucket_negative[int(abs(num))] = [a[i]]
            else: 
                bucket_negative[int(abs(num))] += [a[i]] 
        else:
            if not bucket_positive[int(abs(num))]:
                bucket_positive[int(abs(num))] = [a[i]]
            else: 
                bucket_positive[int(abs(num))] += [a[i]]
    for i in range(bucket_length):
        if bucket_negative[i]:
            bucket_negative[i] = counting_sort(bucket_negative[i])
        if bucket_positive[i]:
            bucket_positive[i] = counting_sort(bucket_positive[i])
    bucket_negative.reverse() 
    res = sum(bucket_negative, []) + sum(bucket_positive, [])
    return res

def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[ (index)%10 ] += 1
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i]

def radixSort(arr): 
  
    # Find the maximum number to know number of digits 
    max1 = max(arr) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1/exp > 0: 
        countingSort(arr,exp) 
        exp *= 10
    return arr

