#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

quantidadeDias = int(input("Quantos dias ficaram com o carro? "))
quantidadeKM = float(input("Quantos KMs foram rodados? "))
precoDia = int(60)
precoKM = float (0.15)
precoTotalDias = (quantidadeDias * precoDia)
precoTotalKM = (quantidadeKM * precoKM)
print precoTotalDias + precoTotalKM
