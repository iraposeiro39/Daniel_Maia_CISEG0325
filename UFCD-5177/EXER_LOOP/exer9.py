#!/bin/python3
# Exercício 9: Escreva um programa que solicite um número ao utilizador até que o valor deste esteja entre
# os valores 1 e 100 (Use o ciclo do ... while)
while True:
    num = int(input("Insira um número entre 1 e 100: "))
    if num <= 100 and num >= 1:
        print(f"obg :) (número inserido: {num})")
        break
    else:
        print("O número tem de estar entre 1 e 100!\n")
