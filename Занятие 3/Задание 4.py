# -- coding: utf-8 --
print('Задание 4')
n=int(input('Введите колличество переменных:'))
s=0
for i in range (n):
    s=s+int(input('Введиете '+str(i+1)+' число: '))
print('Сумма чисел равна ',s)
