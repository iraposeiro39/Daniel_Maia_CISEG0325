#!/bin/python3
# Exemplo básico de um bubble sort
lista = [9, 2, 1, 6, 3, 8, 11, 23, 4, 100, 99123, 11, 0]
count = 0
for i in range(len(lista) - 1):
    for j in range(len(lista) - 1 -i):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            print(lista)
            count += 1
            var = input(f"{count}>")

print(lista)
