#exercicio 011
heightw = float(input('Type the wall`s height in m: '))
basew = float(input('Type the wall`s base in m: '))
areaw = basew * heightw
paintl = areaw / 2
print('The area of the wall is {}m2 \n Considering that each liter of paint covers 2 m2, you`ll need {}L for your wall'.format(areaw, paintl))