#exercicio 017
# jeito mongoloide sem o modulo math
height = float(input('Type the height of a right triangle in cm: '))
base = float(input('Type the base of the same right triangle in cm: '))
hypotenuse = (height ** 2 + base ** 2) ** (1/2)
print('Here you`ll find the values of the triangle \n Height: {}cm \n Base: {}cm \n Hypotenuse: {:.2f}cm'.format(height, base, hypotenuse))

# jeito chad com o modulo math
import math
ht = float(input('Type the height of a right triangle in cm: '))
b = float(input('Type the base of the same right triangle in cm: '))
hp = math.hypot(ht, b)
print('Here you`ll find the values of the triangle \nHeight: {}cm\nBase: {}cm\nHypotenuse: {:.2f}cm'.format(ht, b, hp))