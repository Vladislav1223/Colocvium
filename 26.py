#Напишіть програму аналізу значень температури хворого за добу:
#визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
#температури виробляються шість раз на добу і результати вводяться з клавіатури у
#масив T.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
while True:
    T=np.array(range(1,25,4))#инициализируем масив
    sered=0
    for i in range(len(T)):#проходимся по елементам масива
      T[i] = float(input('Введите температуру'))#Вводим температуру
      sered+=T[i]/len(T)#Ищем среднее значение
    print(T)
    print('Средняя температура',sered)
    minim=min(T)#Ищем минимальное и максимальные значения
    maxim=max(T)
    print('Минимальная',minim,'Максимальная',maxim)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break

