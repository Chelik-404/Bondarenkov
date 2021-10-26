# -- coding: utf-8 --
print('Задание 7')
n=int(input('Введите число: '))
s=1
ss=0
for i in range(1,n+1):
    s*=i
    ss+=s
print ('Факториал данного числа равен:',ss)