# -- coding: utf-8 --
print('Задание 2')
a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
while a==b:
 print('Эти числа не должны быть равны друг другу')
 a=int(input('Введите первое число: '))
 b=int(input('Введите второе число: '))
if a<b:
 for i in range (a,b+1):
   print(i)
else: 
   for i in range (a,b-1,-1):
    print(i)