#Дані про температуру повітря за декаду грудня зберігаються в масиві.
#Визначити, скільки раз температура була вище середньої за цю декаду.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
import random
#Пусть температура ветра за декаду будет от -3 до 3 градусов
while True:
    b=np.zeros(10,dtype=int)#инициализируем масив нулями ,и присваиваем типу данных тип данных инт
    for i in range(10):#проходимся по елементам масив
      b[i] = random.randint(-3,3)
    print(b)
    sered=0
    count=0
    for k in range(10):#снова проходимся по нашей матрице
        sered+=b[k]/10#Ищем среднюю температуру
    for o in range(10):
        if b[o]>sered: #если елементы больше среднего значения,счетчик +1
           count+=1
    print('Средняя температура',sered)
    if count==2 or count==3 or count==4:
      print('Выше была',count,'раза')
    else:
        print('Выше была',count,'раз')
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
