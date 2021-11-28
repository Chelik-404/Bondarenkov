# -- coding: utf-8 --
print('Задание 4')
print()
x=int(input('Введите 1 число : '))
y=int(input('Введите 2 число : '))
k=1
while x<y:
    x+=x/10
    k+=1
print('На',k,'день пробег спортсмена составит не менее',y,'км')