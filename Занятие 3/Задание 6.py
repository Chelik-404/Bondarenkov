# -- coding: utf-8 --
print('Задание 6')
n=int(input('Введите число: '))
s=1
for i in range(1,n+1):
    s*=i
print ('Факториал данного числа равен:',s)