#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

mercadoria = float(input("insira o valor da mercadoria: "))
desconto = float(input("insira o valor do desconto: "))
valorDesconto = mercadoria * desconto / 100
total = mercadoria - valorDesconto
print 'O valor de desconto é: ' , total
