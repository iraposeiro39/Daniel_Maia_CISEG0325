#!/bin/python3
# Exercício 4: Crie um algoritmo que leia um número inteiro, e diga se ele é um número primo ou não.
num1 = int(input("Insira um número: "))

if num1 <= 1:
    print(f"{num1} não é um número primo.")
else:
    primo = True
    for i in range(2, int(num1**0.5) + 1):
        if num1 % i == 0:
            primo = False
            break
    if primo:
        print(f"{num1} é um número primo.")
    else:
        print(f"{num1} não é um número primo.")
