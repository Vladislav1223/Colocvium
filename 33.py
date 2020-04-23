#Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
import random
while True:
    b=np.zeros(20,dtype=int)#инициализируем масив нулями,и присваиваем типу данных тип данных инт
    for i in range(20):#проходимся по елементам масива
      b[i] = random.randint(-2,1)
    print(b)
    dobutok=1
    for k in range(20):#снова проходимся по нашему масиву
       if b[k]!=0:#ищем произведение элементов отличное от нуля
           dobutok*=b[k]
    print(dobutok)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
