# -- coding: utf-8 --
print('Задание 8')

print('Введите первое число')
n1=int(input())
print('Введите второе число')
n2=int(input())
print('Введите третье число')
n3=int(input())

def kol(n1,n2,n3):
 if n1 == n2 and n1 == n3: x=3
 else:
    if n1 == n2 or n1 ==n3 and n2 != n3: x=2
    else: 
     if n2 == n3 or n2 ==n1 and n1 != n3: x=2
     else:
      if n3 == n1 or n3 ==n2 and n2 != n1: x=2
 if n1 != n2 and n2 != n3 and n3 != n1: x=0
 return print(x)

kol(n1,n2,n3)