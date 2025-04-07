#!/bin/python3
# Exercício 13: Elabore um programa que leia um número e mostre a tabuada. (multiplicar de 1 a 10)
num = int(input("Insira um número: "))

for i in range(1,11):
    print(f"{num} x {i} = {num * i}")
