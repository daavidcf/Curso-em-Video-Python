#exercicio 038

firstvalue = float(input('Type a number: '))
secondvalue = float(input('Type a number: '))
if firstvalue > secondvalue:
    print('The first value, {}, is bigger'.format(firstvalue))
elif firstvalue < secondvalue:
    print('The second value, {}, is bigger'.format(secondvalue))
else:
    print('Both values are the same')