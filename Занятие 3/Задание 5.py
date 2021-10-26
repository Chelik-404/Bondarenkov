# -- coding: utf-8 --
print('Задание 5')
n=int(input('Введите натуральное число: '))
s=0
for i in range (1,n+1):
    i=i**3
    s+=i  
print('Сумма кобов равна:',s)