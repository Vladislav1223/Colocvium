#Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
#одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
#числами від 500 до 1000.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
import random
while True:
    b=np.zeros(30,dtype=int)#инициализируем матрицу нулями,и присваеиваем типу данных тип данных инт
    count=0
    for i in range(30):#проходимся по елементам матрицы
      b[i] = random.randint(500,1000)#вводим значения
    print(b)
    for k in range(30):#снова проходимся по нашей матрице
      l=b[k]#помещаем элементы в пустую переменную
      if l%5==0 and l%8==0: 
         count+=l#если значения кратные 5 и 8 
    if count==0:
        print('Таких чисел нету')
    else:
       print('Cумма чисел кратных 5 и 8',count)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break