# -- coding: utf-8 --
print('Задание 4')
S = input('Введите строку: ')
s=(S[S.find(' ')+1:] +' '+ S[:S.find(' ')])
print(s)