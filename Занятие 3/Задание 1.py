# -- coding: utf-8 --
print('Задание 1')
a=int(input('Введите первое число:'))
b=int(input('Введите второе число, которое больше первого:'))
while a>b :
    b=int(input('Ошибка ввода; Введите второе число, которое больше первого:'))
for i in range (a,b+1):
    print(i)
