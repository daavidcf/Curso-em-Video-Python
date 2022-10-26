#exercicio 036

name = str(input('Welcome to the Oaktree Bank property financing system, what is your full name? ')).split()
houseprice = float(input('Nice to meet you, mr. {}! What is the price of the '
                         'property you want to buy? '.format(name[1])))
salary = float(input('Thank you for the information, mr. {}. Now, what is your current salary? '.format(name[1])))
timespan = int(input('Great! Now, one last thing. In how many years you wish to pay off the property? '))
monthlyfee = houseprice / (timespan * 12)
if monthlyfee > salary * 0.30:
    print('I am sorry to inform you that the financing was denied, mr. {}.'
          ' Unfortunately, according to the information provided, the monthly fee would exceed 30% of your current '
          'salary, with a value of {:.2f}.'
          ' In that case, we are not allowed to finance the property.'.format(name[0], monthlyfee))
elif monthlyfee < salary * 0.30:
    print('I am glad to inform you that the financing was approved, mr {}!'
          ' Considering the information provided, you will pay a monthly fee of U${:.2f} during the timespan of '
          '{} years,'
          ' as you have requested.'.format(name[0], monthlyfee, timespan))