#Calcule o tempo de uma viagem de carro. Pergunte a dist�ncia a percorrer e a velocidade m�dia esperada para a viagem.

distancia = float(input("insira o valor da distancia a ser percorrida em KM: "))
velocidadeMedia = float(input("insira o valor da velocidade m�dia: "))
tempototal = distancia / velocidadeMedia
print 'O tempo da viagem ser� de: ' , tempototal, "horas"
