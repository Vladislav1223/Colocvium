#Знайти кількість парних елементів одновимірного масиву.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
import random
while True:
    b=np.zeros(10,dtype=int)#инициализируем масив нулями,и присваиваем типу данных тип данных инт
    count=0
    for i in range(10):#проходимся по елементам масива
      b[i] = random.randint(-10,10)
    print(b)
    for k in range(10):#снова проходимся по нашему масив
       if b[k]%2==0: #если элементы парные,счетчик увеличивается на 1
           count+=1
    print('Количество парных элементов',count)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
