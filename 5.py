#Створіть масив А [1..7] за допомогою генератора випадкових чисел і
#виведіть його на екран. Збільште всі його елементи в 2 рази.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
import random
while True:
    b=np.zeros(7,dtype=int)#инициализируем масив нулями,и присваеиваем типу данных тип данных инт
    u=[]#пустой список для выходного масива
    for i in range(7):#проходимся по елементам матрицы
      b[i] = random.randint(0,100)
    print(b)
    for k in range(7):#снова проходимся по нашей матрице
      l=b[k]*2#помещаем элементы в пустую переменную и умножаем на 2
      u.append(l)#добавляем в список
    print(u)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
