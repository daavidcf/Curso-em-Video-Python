#exercicio 034

salary = float(input('Congratulations, you were awarded with a pay raise, please type your current salary: '))
sraise1 = salary + (salary * 0.10)
sraise2 = salary + (salary * 0.15)

if salary >= 1250.00:
    print('Since your salary is equal or more than U$1250.00, you will get a 10% raise.'
          ' Your new salary is {:.2f}'.format(sraise1))
else:
    print('Since your salary is less than U$1250.00, you will get a 15% raise.'
          ' Your new salary is {:.2f}'.format(sraise2))