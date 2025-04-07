#!/bin/python3
# Exercícios 18: Elabore um programa que leia uma entrada e diga quantos números perfeitos existem.
# Exemplo de numero perfeito em que somando todos os divisores ele da o numero inicial.
# Exemplo: 6=3+2+1
#
limite = int(input("Digite um número: "))
quantidade = 0

for num in range(1, limite + 1):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    if soma == num:
        print(num)
        quantidade += 1

print(f"Existem {quantidade} números perfeitos até {limite}.")
