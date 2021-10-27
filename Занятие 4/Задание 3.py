# -- coding: utf-8 --
print('Задание 3')
S = input('Введите строку: ')
l=int((len(S)+1)/2)
s1=(S[:l])
s2=(S[l:])
print(s2+s1)