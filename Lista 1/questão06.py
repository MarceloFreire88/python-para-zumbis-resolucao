#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input("insira o valor da distancia a ser percorrida em KM: "))
velocidadeMedia = float(input("insira o valor da velocidade média: "))
tempototal = distancia / velocidadeMedia
print 'O tempo da viagem será de: ' , tempototal, "horas"
