# -- coding: utf-8 --
print('Задание 9')
print('Введите колличество долек по вертикали')
n = int(input())
print('Введите колличество долек по горизонтали')
m = int(input())
print()
while n==m:
 print('Колличесвто долек по сторонам не должно быть равно, повторите попытку')
 print()
 n = int(input('Введите колличество долек по вертикали'))
 print()
 m = int(input('Введите колличество долек по горизонтали'))
 print()
k = int(input('Введите колличество долек на отломанном куске'))
if (n * m > k) and  (k % n == 0 or k % m == 0): print('ДА')
else: print('НЕТ')