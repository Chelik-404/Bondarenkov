# -- coding: utf-8 --
print('Задание 3')
print('')

n=int(input('Введите колличество миннут '))
if n>=1440: n-=1440  
h=n//60; m=n%60; print('Время',h,':',m)