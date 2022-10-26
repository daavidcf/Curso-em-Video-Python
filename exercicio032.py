#exercicio 032

year = int(input('Tell me a year of your choice and I will find out if it is a leap year: '))
if (year % 4) == 0:
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))