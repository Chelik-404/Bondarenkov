print('Задание 7')

print('Введите номер года')
n=int(input())

def vs (n):
  if ((n%4) == 0 and n % 100 != 0) or n % 400 == 0: x='ДА'
  else: x='НЕТ'
  return print(x)
vs(n)