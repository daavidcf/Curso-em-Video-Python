#exercicio 035
sides = []
for i in range(0,3):
    lines = int(input('Type three lines in cm and I will tell you if they make up a triangle: '))
    sides.append(lines)
a = sides[0]
b = sides[1]
c = sides[2]

if a + b > c and a + c > b and c + b > a:
    print('The values {}cm, {}cm and {}cm do make up a triangle if needed!'.format(a, b, c))
else:
    print('The values {}cm, {}cm and {}cm do not make up a triangle!'.format(a, b, c))