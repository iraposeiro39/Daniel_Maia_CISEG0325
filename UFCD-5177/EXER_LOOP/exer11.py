#!/bin/python3
# Exercício 11: Elabore um ciclo for para produzir o seguinte output.
# 1
# 22
# 333
num = "1"
for i in range(1,6):
    num_int = num * i
    print(int(num_int) * i)
