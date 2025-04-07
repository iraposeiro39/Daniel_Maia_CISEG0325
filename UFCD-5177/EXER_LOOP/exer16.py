#!/bin/python3
# Exercícios 16: Elabore um programa que constitua a média de 30 números pares que sejam introduzidos.
# Validando a entrada de números inteiros entre 1 e 50.
#
lista = []
for i in range(1, 31):
    while True:
        num = int(input(f"Insira um valor par entre 1 e 50 (nº{i}): "))
        if num % 2 == 0 and num > 0 and num <= 50:
            lista.append(num)
            break
        else:
            print("O valor tem de ser par e estar entre 1 e 50!")

media = sum(lista) / len(lista)
print(f"A média de todos os números inseridos é {media}")
