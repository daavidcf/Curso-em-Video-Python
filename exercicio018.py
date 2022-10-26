#exercicio 018

import math
angleD = float(input('Type an angle for which you want sin, cos and tan: '))
sine = math.sin(math.radians(angleD))
cos = math.cos(math.radians(angleD))
tan = math.tan(math.radians(angleD))
print('The sine of {} is {:.2f}\nIts cos is {:.2f}\nIts tangent is {:.2f}'.format(angleD, sine, cos, tan))