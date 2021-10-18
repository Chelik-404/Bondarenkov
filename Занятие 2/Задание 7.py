# -- coding: utf-8 --
print('Задание 7')

n=int(input('Введите номер года '))

def vs (n):
  if (n%4 == 0 and n % 100 != 0) or n % 400 == 0: print('ДА')
  else: print('НЕТ')
  return
vs(n)