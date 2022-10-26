#Exercicio 037 FAZER DEPOIS

num = int(input('Type a number: '))
print('''Do you want it converted to
[1] Binary
[2] Octal
[3] Hexadecimal''')
option = int(input('Your choice: '))
if option < 1 or option > 3:
    print('Invalid choice!')
elif option == 1:
    print('The number {} converted to binary is {}'.format(num, bin(num)[2:]))
elif option == 2:
    print('The number {} converted to octal is {}'.format(num, oct(num)[2:]))
elif option == 3:
    print('The number {} converted to hexadecimal is {}'.format(num, hex(num)[2:]))
else:
    print('Invalid option!')