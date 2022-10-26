#exercicio 040

name = str(input('Welcome to the school system, teacher! Type your student`s full name: ')).split()
grade1 = float(input('Great! Type mr(s). {} first grade: '.format(name[1])))
grade2 = float(input('Now type mr(s). {} second grade: '.format(name[1])))
average = (grade1 + grade2) / 2

if average < 5:
    print('mr(s). {} average was \033[0;30;41m{:.1f}\033[m. I`m sorry to inform you that the student hasn`t '
          'achieved the necessary grades to '
          'proceed to next year`s class.'.format(name[1], average))
elif average >= 7:
    print('mr(s). {} average was \033[0;97;42m{:.1f}\033[m. I am glad to inform you that the student has achieved'
          ' satisfying grade, '
          'allowing him to proceed to the next year`s class'.format(name[1], average))
else:
    print('mr(s). {} average was \033[0;30;41m{:.1f}\033[m. Unfortunately, they weren`t able to achieve'
          ' satisfying grades to proceed to '
          'next year`s classes.'
          ' Nevertheless, the student will be allowed to'
          ' take another month of classes and try again'.format(name[1], average))