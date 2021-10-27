# -- coding: utf-8 --
print('Задание 7')
S = input('Введите строку: ')
print(S[:S.find('h')]+S[S.rfind('h')+1:])