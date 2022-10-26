#exercicio 022

name = input('Please, type your name: ').strip()
print('This is your name with all letters on upper case: {}'.format(name.upper()))
print('This is your name with all letters on lower case: {}'.format(name.lower()))
print('Your name has {} letters'.format(len(name) - name.count(' ')))
splitname = name.split()
print('Your first name has {} letters'.format(name.find(' ')))
print('Welcome {}!'.format(splitname[0]))