#!/bin/python3
# Exercício 12: Elabore um programa que leia quantos números quer que se efetue a soma, subtrações,
# divisões, multiplicações e no fim por meio de um acumulador diga quantas operações foram efetuadas.
# Exemplo introduzindo o número 60 o programa deve apresentar 60 a somar, dividir multiplicar e subtrair
# por todos os números menores que ele.
#
contador = 0
num = int(input("Insira um número: "))

for i in range(1,num):
    print("=======================")
    print(f"{num} + {i} = {num+i}")
    print(f"{num} / {i} = {num/i}")
    print(f"{num} * {i} = {num*i}")
    print(f"{num} - {i} = {num-i}")
    print("=======================")
    contador = contador + 4

print(f"Foram efetuadas {contador} operações!")
