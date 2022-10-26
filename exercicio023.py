#exercicio 023

#Metodo string
usernum = int(input('Type a number between 0 and 9999: '))
if usernum < 0 or usernum > 9999:
    print('Invalid number!')
else:
    n = str(usernum)
    print('Let`s divide the number provided, which is {}'.format(usernum))
    print('Fourth character: {}'.format(n[3]))
    print('Third character: {}'.format(n[2]))
    print('Second character: {}'.format(n[1]))
    print('First character: {}'.format(n[0]))

#Metodo int

num = int(input('Type a number between 0 and 9999: '))
if num < 0 or num > 9999:
    print('Invalid number!')
else:
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print('Let`s analyse the number provided: {}'.format(num))
    print('Fourth character: {}'.format(u))
    print('Third character: {}'.format(d))
    print('Second character: {}'.format(c))
    print('First character: {}'.format(m))