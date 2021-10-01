print('Задание 3')
a=int(input('Введите первое число:'))
b=int(input('Введите второе число, которое меньше первого:'))
while a<=b :
    b=int(input('Ошибка ввода; Введите второе число, которое меньше первого:'))
if a%2!=0:
 for i in range (a,b-1,-2):
    print(i)
else: 
 for i in range (a-1,b-1,-2):
    print(i)