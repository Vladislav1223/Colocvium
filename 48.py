#Наведено список прізвищ брокерів товарної біржі з N чоловік. Поміняйте
#місцями прізвища брокерів: першого і останнього, другого і передостаннього, третього
#з початку і третього від кінця і т.д.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
while True:
   n = int(input("Введите количество брокеров "))
   b = np.zeros(n, dtype=object)#инициализируем масив нулями,и укзываем тип даных object(Что бы масив собой представлял масив строк)
   for i in range(n):#Вводим элементы масива
     b[i] = input("Введите фамилию: ")
   print(b)
   print(b[::-1])#Выводим наш масив в обратном порядке с помощью среза
   result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
   if result == '1':
        continue
   else:
        break