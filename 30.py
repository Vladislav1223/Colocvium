#Обчислити середнє арифметичне значення тих елементів одновимірного
#масиву, які розташовані за першим по порядку мінімальним елементом.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
import random
while True:
    b=np.zeros(5,dtype=int)#инициализируем масив нулями,и присваиваем типу данных тип данных инт
    for i in range(5):#проходимся по елементам масива
      b[i] = random.randint(1,100)
    print(b)
    count=0
    u=[]
    count1=0
    minim=min(b)
    for k in range(5):
        if b[k]==min(b):
            count=k #Ищем индекс минимального числа
    for l in range(5):
        if l>count:#ищем индексы чисел после минимального и добавим их в список
            u.append(b[l])
    print(u)
    if len(u)==0: #Если длинна списка 0,значит минимальный элемент на последней позиции,и элементов за ним нету.Соотвествено и сумма 0
        print('Сумма 0')
    else:
        print('Среднее значение после минимального',sum(u)/len(u))
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
