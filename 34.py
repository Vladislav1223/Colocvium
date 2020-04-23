#Дано два лінійних масиву однакової розмірності. Скласти третій масив з
#добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
import random
while True:
    b=np.zeros(5,dtype=int)#инициализируем  масив нулями,и присваиваем типу данных тип данных инт
    a=np.zeros(5,dtype=int)
    for i in range(5):#проходимся по елементам матрицы
      b[i] = random.randint(-5,5)
      a[i]=random.randint(-5,5)
    print(b)
    print(a)
    ab=np.zeros(5,dtype=int)
    for k in range(5):
        ab[k]=b[k]*a[k] #Выполняем поэлементное умножение двух масивов
    print('Третий масив',ab)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
