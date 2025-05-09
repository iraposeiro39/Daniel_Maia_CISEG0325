#!/bin/python3
# Classes
class Barcos:
    def __init__(self,nome,ano,carga,carga_max,velocidade):
        self.nome = nome
        self.ano = ano
        self.carga = carga
        self.carga_max = carga_max
        self.velocidade = velocidade

    def AumentarCarga(self,carga_adicional):
        if self.carga + carga_adicional > self.carga_max:
            print("Não é possivel adicionar mais carga! ")
        else:
            self.carga += carga_adicional

    def Acelerar(self,nivel):
        match nivel:
            case 1:
                self.velocidade += 10
            case 2:
                self.velocidade += 15
            case 3:
                self.velocidade += 20

    def Travar(self,nivel):
        match nivel:
            case 1:
                self.velocidade -= 10
            case 2:
                self.velocidade -= 15
            case 3:
                self.velocidade -= 20

# Dados do Barco
barco1 = Barcos("Zé Ferreira", 1976, 3600, 15000, 0)

# Carga
print(f"Carga do Barco {barco1.nome}: {barco1.carga}")
barco1.AumentarCarga(10000)
print(f"Carga do Barco {barco1.nome}: {barco1.carga}")

# Velocidade
print(f"Velocidade do Barco {barco1.nome}: {barco1.velocidade}")
barco1.Acelerar(2)
print(f"Velocidade do Barco {barco1.nome}: {barco1.velocidade}")
barco1.Travar(2)
print(f"Velocidade do Barco {barco1.nome}: {barco1.velocidade}")
barco1.Acelerar(3)
print(f"Velocidade do Barco {barco1.nome}: {barco1.velocidade}")

# Dados Finais do Barco
print("== Barco nº1 ==")
print(f"Nome: {barco1.nome}")
print(f"Ano: {barco1.ano}")
print(f"Carga Presente: {barco1.carga}")
print(f"Carga Máxima: {barco1.carga_max}")
print(f"Velocidade: {barco1.velocidade}")
