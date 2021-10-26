# -- coding: utf-8 --
print('Задание 9')
n = int(input('Введите число: '))
f1 = f2 = 1
s=0
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    s+=f2
print('Сумма',n,'чисел фибоначчи равна:',s+2)