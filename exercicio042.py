#exercicio 042

sides = []
for i in range(0, 3):
    lines = int(input('Type three lines in cm and I will tell you if they make up a triangle: '))
    sides.append(lines)
a = sides[0]
b = sides[1]
c = sides[2]

if a + b > c and a + c > b and c + b > a:
    print('The values {}cm, {}cm and {}cm do make up a triangle if needed!'.format(a, b, c))
    if a == b == c:
        print('The triangle formed by these lines is an equilateral triangle!')
    elif a == b and a != c:
        print('The triangle formed by these lines is an isosceles triangle!')
    elif a == c and a != b:
        print('The triangle formed by these lines is an isosceles triangle!')
    elif b == c and b != a:
        print('The triangle formed by these lines is an isosceles triangle!')
    else:
        print('The triangle formed by these lines is a Scalene triangle!')
else:
    print('The values {}cm, {}cm and {}cm do not make up a triangle!'.format(a, b, c))