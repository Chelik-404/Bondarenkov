# -- coding: utf-8 --
print('Задача 4')
second= 23452356
days= second /60/60//24
hours=second //60//60%24
minutes = second//60%60
sec=second%60
print('Дни:',days,'Часы:',hours,'Минуты:',minutes,'Секунды:',sec)