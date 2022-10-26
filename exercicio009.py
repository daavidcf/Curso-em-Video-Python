#exercicio 009
usernumber = int(input('Type the number whose multiplication table you want: '))
if usernumber > 9 or usernumber < 1:
    print('Invalid option, please type a number between 1 and 9')
else:
    print('Here is the multiplication table for', usernumber, ':')
    print(usernumber, 'X 1 =', usernumber * 1)
    print(usernumber, 'X 2 =', usernumber * 2)
    print(usernumber, 'X 3 =', usernumber * 3)
    print(usernumber, 'X 4 =', usernumber * 4)
    print(usernumber, 'X 5 =', usernumber * 5)
    print(usernumber, 'X 6 =', usernumber * 6)
    print(usernumber, 'X 7 =', usernumber * 7)
    print(usernumber, 'X 8 =', usernumber * 8)
    print(usernumber, 'X 9 =', usernumber * 9)