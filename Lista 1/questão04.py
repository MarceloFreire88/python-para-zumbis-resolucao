#Fa�a um programa que calcule o aumento de um sal�rio. Ele deve solicitar o valor do sal�rio e a porcentagem do aumento. Exiba o valor do aumento e do novo sal�rio.

salarioAtual =float (input("Qual � o seu sal�rio?  "))
procetagemDeAumento = int (input("Quanto � a porcetagem de aumento? "))
aumento = salarioAtual * procetagemDeAumento
novoSalario = int(salarioAtual + (salarioAtual* procetagemDeAumento / 100))

print 'Seu aumento �: ', aumento, 'e', 'Seu novo sal�rio �:', novoSalario
