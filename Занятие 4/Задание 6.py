# -- coding: utf-8 --
print('Задание 6')
S = input('Введите строку: ')
F=S.find('f')
f=S.count('f')
if f==0:print('-2')
if f==1:print('-1')
if f>1:print('Индекс второго символа "f" равен:',S.find('f',F+1))