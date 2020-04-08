# Implementação de algoritmos de ordenação

Nesse repositório, encontram-se implementados os algoritmos de ordenação Insertion Sort e Selection Sort. O programa recebe um arquivo com números inteiros, onde o primeiro número mostra a quantidade de números subsequentes, e retorna uma sequência de números inteiros ordenados. O programa principal é o sort.py, escrito em Python 3, e tem como dependências as bibliotecas pandas, numpy e argparse. O software têm um menu ajuda, como descrito a seguir:

```
python sort.py -h
usage: sort.py [-h] [-f LIST_INTEGERS] [-s] [-i] [--version]

optional arguments:
  -h, --help        show this help message and exit
  -f LIST_INTEGERS  Arquivo com os números a serem ordenados
  -s                Algoritmo selection sort selecionado
  -i                Algoritmo insertion sort selecionado
  --version         show program's version number and exit
```

Por exemplo, caso queira ordenar um arquivo com 1000 números utilizando o algoritmo insertion sort, os parâmetros de entrada no console seriam assim:

```
python sort.py -f instancias-num/num.1000.1.in -i
```
