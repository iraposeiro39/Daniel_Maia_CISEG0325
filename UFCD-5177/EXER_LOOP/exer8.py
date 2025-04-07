#!/bin/python3
# Exercício 8: Faça um algoritmo que gere a seguinte série: 10, 20, 30, 40, ..... 980, 990, 1000.
# E outro a fazer 15, 25, 35, 985, 995. (dois ciclos)
#
# 10 em 10, a começar no 10
for i in range(1,1001):
    if i % 10 == 0:
        print(i)

# 10 em 10 a começar no 15
for i in range(1,1001):
    if i % 10 == 0:
        print(i+5)
