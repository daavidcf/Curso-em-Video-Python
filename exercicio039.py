#exercicio 039

age = int(input('Welcome to the American Army website, how old are you: '))
timeleft = 18 - age
urlate = age - 18
if age < 18:
    print('You are too young to join the army, wait until you are 18!')
    print('Currently, you must wait {} years before your compulsory enlistment'.format(timeleft))
elif age == 19:
    print('You are late! You should have joined the army already!')
    print('You should have made yourself present at the nearest outpost a year ago')
elif age > 19:
    print('You are late! Yoy should have joined the army already!')
    print('You should have made yourself present at the nearest outpost {} years ago'.format(urlate))
else:
    print('Congratulations mf, you are 18! It`s time to join the army, come to the nearest outpost')