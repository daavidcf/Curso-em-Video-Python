#exercicio 030

usern = int(input('Tell me a number and I`ll tell you if it is even or odd: '))
if (usern % 2) == 0:
    print('{} is an even number'.format(usern))
else:
    print('{} is an odd number'.format(usern))