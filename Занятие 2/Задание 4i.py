# -- coding: utf-8 --
print('Задание 4.i')
print('')

def i4 (a,b,l,n): 

 return print('Длина шнурка должна быть равна',(l*2)+(a*n*2-a)+(b*(n-1)*2))

print('Введите расстояние между рядами шнурков')
a=int(input())
print('Введите расстояние между дырочками в ряду')
b=int(input())
print('Введите длину свободного конца шнурка')
l=int(input())
print('Введите количество дырочек в каждом ряду')
n=int(input())
 
i4(a, b, l, n)