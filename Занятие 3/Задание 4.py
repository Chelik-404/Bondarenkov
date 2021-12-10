# -- coding: utf-8 --
print('Задание 4')
s=0
for i in range (int(input('Введите колличество переменных: '))):
    s=s+int(input('Введите '+str(i+1)+' число: '))
print('Сумма чисел равна ',s)