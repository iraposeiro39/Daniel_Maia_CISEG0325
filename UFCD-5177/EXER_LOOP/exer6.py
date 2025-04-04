#!/bin/python3
# Exercício 6: Crie um algoritmo que mostre os 10 primeiros números primos.
contador = 0
num = 2

while contador < 10:
    primo = True
    if num <= 1:
        primo = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                primo = False
                break
    if primo:
        print(num)
        contador += 1
    num += 1
