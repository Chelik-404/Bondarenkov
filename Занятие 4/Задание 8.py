# -- coding: utf-8 --
print('Задание 8')
S =input('Введите строку: ')
print(S[:S.find('h')]+S[S.rfind('h'):S.find('h'):-1]+S[S.rfind('h'):])