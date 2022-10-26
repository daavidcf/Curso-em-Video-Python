# exercicio 007
name = str(input('Type the student`s name: '))
grade1 = float(input('Type the student`s first grade: '))
grade2 = float(input('Type the student`s second grade: '))
average = (grade1 + grade2) / 2
print('Here are the grades by student {} during the semester: \n First grade: {} \n Second grade: {}'.format(name, grade1, grade2))
print('His average score is: {}'.format(average))
if average > 7.0:
    print('Student {} has scored enough to be approved into the next class!'.format(name))
else:
    print('Student {} did not achieve the necessary score to get in the next class.'.format(name))