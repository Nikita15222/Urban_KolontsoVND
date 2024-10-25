from time import sleep
from random import randint
n1, n2 = int(input('Вбейте начальную цифру диапазона: ')), int(input('Вбейте конечную цифру диапазона: '))
n = randint(n1,n2)
sleep(0.5)
print(f'Угадайте число от {n1} до {n2}')
t = int(input())
if t == n:
    print('Угадали! Вы молодцы!')
else:
    while t != n:
        if t < n:
            print('Ваше число меньше загаданного')
            t = int(input("Попробуйте еще раз: "))
            if t == n:
                print('Угадали! Вы молодцы!')
        else:
            print('Ваше число больше загаданного')
            t = int(input("Попробуйте еще раз: "))
            if t == n:
                print('Угадали')