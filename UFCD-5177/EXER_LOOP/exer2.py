#!/bin/python3
# Exercício 2: Ler 10 números, e determinar se o número par e número impar.
for i in range(1,11):
    if i % 2 == 0:
        print(f"par: {i}")
    if i % 2 == 1:
        print(f"impar: {i}")
