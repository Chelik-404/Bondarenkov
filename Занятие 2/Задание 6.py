print('Задание 6')
print()

a=[['Белый','Коричневый','Белый','Коричневый','Белый','Коричневый','Белый','Коричневый'],
['Коричневый','Белый','Коричневый','Белый','Коричневый','Белый','Коричневый','Белый'],
['Белый','Коричневый','Белый','Коричневый','Белый','Коричневый','Белый','Коричневый'],
['Коричневый','Белый','Коричневый','Белый','Коричневый','Белый','Коричневый','Белый'],
['Белый','Коричневый','Белый','Коричневый','Белый','Коричневый','Белый','Коричневый'],
['Коричневый','Белый','Коричневый','Белый','Коричневый','Белый','Коричневый','Белый'],
['Белый','Коричневый','Белый','Коричневый','Белый','Коричневый','Белый','Коричневый'],
['Коричневый','Белый','Коричневый','Белый','Коричневый','Белый','Коричневый','Белый']]
def srav (c,v,b,q):
 if a[c][v] in a[b][q]: x='ДА'
 else: x='НЕТ'
 return print(x)

print('Введите номер строки первой ячейки(от 1 до 8)')
y1=int(input())
while y1<1 or y1>8:
 print('Номер не соответсвует границам,введите номер строки первой ячейки(от 1 до 8)')
 y1=int(input())
y1-=1
print('Введите номер столбца первой ячейки(от 1 до 8)')
y2=int(input())
while y1<1 or y1>8:
 print('Номер не соответсвует границам,введите номер столбца первой ячейки(от 1 до 8)')
 y1=int(input())
y2-=1
print('Введите номер строки второй ячейки(от 1 до 8)')
y3=int(input())
while y1<1 or y1>8:
 print('Номер не соответсвует границам,введите номер строки второй ячейки(от 1 до 8)')
 y1=int(input())
y3-=1
print('Введите номер столбца второй ячейки(от 1 до 8)')
y4=int(input())
while y1<1 or y1>8:
 print('Номер не соответсвует границам,введите номер столбца второй ячейки(от 1 до 8)')
 y1=int(input())
y4-=1

srav(y1,y2,y3,y4)