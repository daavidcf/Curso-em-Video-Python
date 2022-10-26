#exercicio 029
import random
n = random.randint(40, 84)
if n < 60:
    print('Your speed at the moment you passed by the camera was {}km/h, '
          'therefore no law infringement was committed'.format(n))
else:
    if n > 60 and n < 72:
        print('Your speed caught by camera was {}km/h, therefore you were up to 20% above the speed limit for'
              ' the highway. You will get a ticket of U$50 for this infringement.'.format(n))
    if n > 72 and n < 84:
        print('Your speed caught by camera was {}km/h, therefore you were up to 20% above the speed limit for'
              ' the highway. You will get a ticket of U$75 for this infringement.'.format(n))
print('City Traffic Institution, always at your service!')

import random
speed = random.randint(60, 100)
ticket = (speed - 80) * 7
if speed > 80:
    print('Considering the 80km/h speed limit, and your {}km/h speed at the moment you passed by the camera'
          ' you will get a U${} ticket for the infringement.'.format(speed, ticket))
else:
    print('Considering the 80km/h speed limit, and your {}km/h speed at the moment you passed by the camera'
          ', no infringement was committed, good job!'.format(speed))