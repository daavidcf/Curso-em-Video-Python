#exercicio 010
money = float(input('Type how much money you have in your wallet(R$): '))
moneyD = money * 3.27
print('Considering U$ 1.00 = R$3.27, you can buy U${} with your R${}'.format(moneyD, money))