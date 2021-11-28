# -- coding: utf-8 --
print('Задание 2')
print()
n=int(input('Введите число >=2: '))
i=2
while i!=n+1:
    if n%i==0:
     print('Наименьший дилитель числа',n,'равен:',i)
     break
    i+=1