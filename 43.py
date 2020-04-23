#Задано два натуральних числа a і b. Змінній w привласнити значення
#істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
#і не кратний b.
import numpy as np#импортируем библиотеку нампи 
import random
while True:
    a=int(input('Введите a: '))
    b=int(input('Введите b: '))
    o=np.zeros(10,dtype=int)#инициализируем масив нулями,и присваеиваем типу данных тип данных инт
    w=False
    for i in range(10):#проходимся по елементам матрицы
      o[i] = random.randint(5,30)#вводим значения
    print(o)
    for k in range(10):
        if o[k]%a==0 and o[k]%b!=0:
            w=True
    print(w)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
