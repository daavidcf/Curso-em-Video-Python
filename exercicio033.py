#exercicio 033

list = []
for i in range(0,3):
    usern = (int(input('Type three numbers: ')))
    list.append(usern)
hnum = max(list)
lnum = min(list)
print('The highest number amongst the three is {} and the lowest is {}'.format(hnum, lnum))