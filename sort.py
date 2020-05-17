import argparse

import pandas as pd

import bib

parser = argparse.ArgumentParser()

parser.add_argument('-f', action='store', dest='list_integers', help='Arquivo com os números a serem ordenados')
parser.add_argument('-s', action='store_const', dest='sort_method', const='selection', help='Algoritmo selection sort selecionado')
parser.add_argument('-i', action='store_const', dest='sort_method', const='insertion', help='Algoritmo insertion sort selecionado')
parser.add_argument('-q', action='store_const', dest='sort_method', const='quick', help='Algoritmo quick sort selecionado')
parser.add_argument('-m', action='store_const', dest='sort_method', const='merge', help='Algoritmo merge sort selecionado')
parser.add_argument('-c', action='store_const', dest='sort_method', const='count', help='Algoritmo count sort selecionado')
parser.add_argument('-b', action='store_const', dest='sort_method', const='bucket', help='Algoritmo bucket sort selecionado')
parser.add_argument('-r', action='store_const', dest='sort_method', const='radix', help='Algoritmo radix sort selecionado')
parser.add_argument('-mhp', action='store_const', dest='sort_method', const='max_heap', help='Algoritmo heap máximo selecionado')
parser.add_argument('-hp', action='store_const', dest='sort_method', const='heap', help='Algoritmo heap sort selecionado')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()

data = pd.read_csv(results.list_integers, header=None)
arr = data.to_numpy().ravel()
res = []

if(results.sort_method == 'selection'):
    res = bib.selection_sort(arr[1:])
elif(results.sort_method == 'insertion'):
    res = bib.insertion_sort(arr[1:])
elif(results.sort_method == 'count'):
    res = bib.counting_sort(arr[1:])
elif(results.sort_method == 'radix'):
    res = bib.radix_sort(arr[1:])
elif(results.sort_method == 'bucket'):
    res = bib.bucket_sort(arr[1:])
#elif(results.sort_method == 'merge'):
#    res = bib.merge_sort(arr[1:])
#elif(results.sort_method == 'quick'):
#    res = bib.quickSort(arr[1:], 0, len(arr)-1)

elif results.sort_method == 'max_heap':
    res = bib.build_max_heap(arr[1:])

elif results.sort_method == 'heap':
    res = bib.heap_sort(arr[1:])

for i in range(len(res)):
    print(res[i])