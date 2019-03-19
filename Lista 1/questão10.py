#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarroFumados = int(input("Quantos cigarros por dia você fumou? "))
anosFumados = int(input("Quantos anos da sua vida você fumou? "))
totalFumando = (anosFumados * 365) * cigarroFumados
diasPerdidos = (totalFumando * 10)/24

print 'seu total de dias perdidos é: ', diasPerdidos
