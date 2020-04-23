#Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
#за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
while True:
   n = int(input("Введіть кількість послуг: "))
   a = np.zeros(n,dtype=object)#инициализируем масив нулями,и укзываем тип даных object(Что бы масив собой представлял масив строк)
   b = np.zeros(n,dtype=int)
   for i in range(n):
    a[i] = input("Введіть послугу: ")
    b[i] = int(input("Введіть ціну: "))
   print(a)
   print(b)
   poslug=0
   count=0
   G = int(input("Введіть ціну G: "))
   for i in range(n):
     if G == b[i]:#Если элемент равен заданой цене,то все следующие элементы удаляем с 2 таблиц
        poslug = a[i:]
        count = b[i:]
   print(poslug)
   print(count)
   result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
   if result == '1':
        continue
   else:
        break

