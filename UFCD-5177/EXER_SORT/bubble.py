#!/bin/python3
# Exemplo básico de um bubble sort
lista = [9, 2, 1, 6, 3, 8, 11, 23, 4, 100, 99123, 11, 0]
tmp = 0

for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] > lista[j+1]:
            tmp = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = tmp

print(lista)
