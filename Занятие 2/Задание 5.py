# -- coding: utf-8 --
print('Задание 5')
print()
  
def min (a,b,c):
 if a<b: m=a
 else: m=b
 if c<m: m=c
 return print('Минимальное число равно',m)

print('Введите 1 число')
a=int(input())
print('Введите 2 число')
b=int(input())
print('Введите 3 число')
c=int(input())

min(a,b,c)