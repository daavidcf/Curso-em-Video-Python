#exercicio 041

name = str(input('Welcome to the national swimming association. What is your name? '))
age = int(input('Nice to meet you, {}! Now, how old are you? '.format(name)))
if age <= 9:
    print('Thank you, {}! You will be part of the children team!'.format(name))
elif age > 9 and age <= 14:
    print('Thank you, {}! You will be part of the early teens team!'.format(name))
elif age > 14 and age <= 18:
    print('Thank you, {}! You will be part of the late teens team!'.format(name))
elif age >= 19 and age <= 20:
    print('Thank you, {}! You will be part of the senior team!'.format(name))
else:
    print('Thank you, {}! You will be part of the master team!'.format(name))