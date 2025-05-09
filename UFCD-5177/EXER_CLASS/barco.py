#!/bin/python3
# Classes
class Barcos:
    def __init__(self,nome,ano,carga,carga_max,velocidade):
        self.nome = nome
        self.ano = 0
        self.carga = carga
        self.carga_max = carga_max
        self.velocidade = velocidade

    def getNome(self):
        return self.nome

    def getAno(self):
        return self.ano

    def getCarga(self):
        return self.carga

    def sumCarga(self,carga):
        self.carga += carga

    def getCarga_max(self):
        return self.carga_max

    def getVelocidade(self):
        return self.velocidade

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
print(f"Carga presente: {barco1.getCarga()}")
print(f"Carga Máxima: {barco1.getCarga_max()}")
num = int(input("Quanta carga é que pretendes adicionar ao barco?(kg): "))
if barco1.getCarga() + num > barco1.getCarga_max():
    print("Não é possivel adicionar tanta carga ao barco!")
else:
    barco1.sumCarga(num)
print(f"Carga após adicionar: {barco1.getCarga()}")

# Velocidade
print(f"Velocidade do Barco {barco1.getNome()}: {barco1.getVelocidade()}")
barco1.Acelerar(2)
print(f"Velocidade do Barco {barco1.getNome()}: {barco1.getVelocidade()}")
barco1.Travar(2)
print(f"Velocidade do Barco {barco1.getNome()}: {barco1.getVelocidade()}")
barco1.Acelerar(3)
print(f"Velocidade do Barco {barco1.getNome()}: {barco1.getVelocidade()}")

# Dados Finais do Barco
print("== Barco nº1 ==")
print(f"Nome: {barco1.getNome()}")
print(f"Ano: {barco1.getAno()}")
print(f"Carga Presente: {barco1.getCarga()}")
print(f"Carga Máxima: {barco1.getCarga_max()}")
print(f"Velocidade: {barco1.getVelocidade()}")
