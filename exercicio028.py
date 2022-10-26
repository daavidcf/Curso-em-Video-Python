#exercicio 028
import random
n = random.randint(0, 5)
un = int(input('I just thought of a number 0 and 5, guess which it is: '))
if un < 0 or un > 5:
    print('Invalid number! Game over')
else:
    if un == n:
        print('Correct number, you win...')
    else:
        print('Lmao not this one bruh, it was {} haha u lost xD'.format(n))