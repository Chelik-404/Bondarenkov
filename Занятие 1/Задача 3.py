# -- coding: utf-8 --
print('Задача 3')
age = int(input('Введите свой возраст '))
if age>0 and age<75:
 if age>=16:
  name=str(input('Введите своё имя '))
  if name == 'Иван': print('Недопустимое имя')
  else: print('Поздравляем вы поступили в ВГУИТ')
 else: print('Сначала нужно окончть школу! Вам нужно еще '+str(16-age)+' учиться в школе')
else: print('Недопустимый возраст')