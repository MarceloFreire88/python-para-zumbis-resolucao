#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salarioAtual =float (input("Qual é o seu salário?  "))
procetagemDeAumento = int (input("Quanto é a porcetagem de aumento? "))
aumento = salarioAtual * procetagemDeAumento
novoSalario = int(salarioAtual + (salarioAtual* procetagemDeAumento / 100))

print 'Seu aumento é: ', aumento, 'e', 'Seu novo salário é:', novoSalario
