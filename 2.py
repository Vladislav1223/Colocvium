#Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
#екран значення коріння і квадратів кожного з елементів масиву.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
while True:
    b=np.zeros(5,dtype=int)#инициализируем матрицу нулями,и присваеиваем типу данных тип данных инт
    u=[]#пустой список для выходного масива
    u1=[]
    for i in range(5):#проходимся по елементам матрицы
      b[i] = int(input('Введите ваши элементы: '))#вводим значения
    for k in range(5):#снова проходимся по нашей матрице
      l=b[k]**2 # подносим к квадрату
      l1=b[k]**0.5 #корень
      u.append(l)#добавляем в список квадрат
      u1.append(l1)# добавляем в список корень
    print('Значения в квадрате',u)
    print('Корень',u1)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break

