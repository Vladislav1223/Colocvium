#У лінійному масиві знайти максимальний елемент. Вставте порядковий
#номер елемента за ним, пересунувши всі залишилися на одну позицію вправо.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
import random
while True:
    b=np.zeros(15,dtype=int)#инициализируем матрицу нулями,и присваиваем типу данных тип данных инт
    for i in range(15):#проходимся по елементам матрицы
      b[i] = random.randint(-15,15)
    print(b)
    a=0
    u=[]
    g=[]
    p=[]
    vse=[]
    for k in range(15):
        if b[k]>a: #Пустое значение а,поэлементно принимает значения с масива,до тех пор,пока не найдется макимальное
            a=b[k]
            count=k#Наш счетчик принимает значение индексов 
    for o in range(15):
        if o<=count: #По индексам элементы слева от максимального значения и само максимальное значение,помещаем в один список
            u.append(b[o])
            if o==count:#Помещаем индекс максимального значения в отдельный список(это будет наш номер)
             g.append(o)
        else:
            p.append(b[o])#Елементы справа тоже помещаем в список
    vse=u+g+p#По порядку складываем 3 наших списка в 1
    print(vse)
    print('Индекс',count)
    print('Число',a)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
