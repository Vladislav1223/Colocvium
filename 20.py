#Знайти суму всіх елементів масиву дійсних чисел, більших за задане
#число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
#від 50 до 100.
#Павлюк Владислав
#Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
#масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
import random
while True:
    x=int(input('Введите число для сравнения:'))
    b=np.zeros(20,dtype=float)#инициализируем матрицу нулями,и присваеиваем типу данных тип данных флоат
    count=0
    for i in range(20):#проходимся по елементам матрицы
      b[i] = random.uniform(50,100)#вводим значения,где uniform представляет заполнение числами типа(Float)
    print(b)
    for k in range(20):#снова проходимся по нашей матрице
      if b[k]>x: #Если элементы больше за наше число
         count+=l#если  значения больше х,складываем их
    if count==0:
         print('Таких чисел не существует')
    else:
         print('Сумма єлементов',count)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
