#exercicio 031

tripd = int(input('Tell me the distance of your trip in km: '))
t1 = tripd * 0.50
t2 = tripd * 0.45
if tripd < 200:
    print('Considering that the ticket price consists of U$0.50 for each km in case of trips under 200km, '
          'your ticket will cost U${}'.format(t1))
else:
    print('Considering that the ticket price consists of U$0.45 for each km in case of trips over 200km, '
          'your ticket will cost U${}'.format(t2))