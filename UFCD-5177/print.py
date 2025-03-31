#!/bin/python3
# PRINT
# Vem por default com um espaço entre os inputs
print("Hello","World")
# Vem com um separator definido pelo user
print("Hello","World", sep = "<>")
# Em vez de dar print de \n (newline) dá print de fixe (sem trocar de linha, já que trocamos o \n por fixe)
print("Hello","World", end = "fixe")
# Print no end com 3 newlines
print("Hello","World", end = "\n\n\n")
# Print de variavel dentro de um print com a flag formattable
smile = ":)"
print(f"Boas Bro {smile}")
#
# PRINT com PEP-8 (?)
# Variáveis que vamos usar
num_tel = 962849223
name_cli = "Garbiel Caiadas"
#
# Print para demonstrar os detalhes do cliente desformatado
print("Desformatado")
print("Nome do Cliente:",name_cli,"Num. Telefone:",num_tel)
#
# Print para demonstrar os detalhes do cliente em 2 linhas
# a flag "\n" tem de sempre fazer parte de uma string para ter efeito
print("\nFormatado")
print("Nome do Cliente:",name_cli,"\nNum. Telefone:",num_tel)
