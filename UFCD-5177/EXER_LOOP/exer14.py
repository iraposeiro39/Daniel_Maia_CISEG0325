#!/bin/python3
# Exercício 14: Altere o programa anterior para que mostre todas as tabuadas de 1 a 100. (ciclos for).
num = int(input("Insira um número: "))

for i in range(1,101):
    print(f"{num} x {i} = {num * i}")
