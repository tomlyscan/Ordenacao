# Implementação de algoritmos de ordenação

Nesse repositório, encontram-se implementados os algoritmos de ordenação Insertion Sort e Selection Sort. O programa recebe um arquivo com números inteiros, onde o primeiro número mostra a quantidade de números subsequentes, e retorna uma sequência de números inteiros ordenados. O programa principal é o sort.py, escrito em Python 3, e tem como dependências as bibliotecas pandas, numpy e argparse. O software têm um menu ajuda, como descrito a seguir:

```
python sort.py -h
usage: sort.py [-h] [-f LIST_INTEGERS] [-s] [-i] [-q] [-m] [-c] [-b] [-r] [-mhp] [-hp] [--version]

optional arguments:
  -h, --help        show this help message and exit
  -f LIST_INTEGERS  Arquivo com os números a serem ordenados
  -s                Algoritmo selection sort selecionado
  -i                Algoritmo insertion sort selecionado
  -q                Algoritmo quick sort selecionado
  -m                Algoritmo merge sort selecionado
  -c                Algoritmo count sort selecionado
  -b                Algoritmo bucket sort selecionado
  -r                Algoritmo radix sort selecionado
  -mhp              Algoritmo heap máximo selecionado
  -hp               Algoritmo heap sort selecionado
  --version         show program's version number and exit
```

Por exemplo, caso queira ordenar um arquivo com 1000 números utilizando o algoritmo insertion sort, os parâmetros de entrada no console seriam assim:

```
python sort.py -f instancias-num/num.1000.1.in -i
```
- Funções T(n) do Insertion Sort:

  Para o melhor caso (lista ordenada), o algoritmo precisa passar por cada elemento uma vez com exceção do primeiro. Então, t(n) = n - 1.

  Para o pior caso (lista invertida), o algoritmo precisa percorrer a lista novamente para cada elemento dela. Logo, t(n) = n*n
  
- Funções T(n) do Selection Sort:
  O algoritmo busca sempre encontrar o valor mínimo (ou máximo) da lista e colocá-lo em uma outra ordenada. Dessa forma, ele sempre vai percorrer a lista para cada elemento, mas a quantidade de elementos na lista original vai reduzindo a medida que irá sendo ordenado. Dessa forma, T(n) = n * (n-1)/2.
