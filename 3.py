#Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
#починаючи з останнього.
#Павлюк Владислав 
import numpy as np#импортируем библиотеку нампи
while True:
    b=np.array([input('Введите фамилию: ') for i in range(5)]) #Заводим масив,и вводиим в масив  5 значений
    for k in range(5):#снова проходимся по нашей матрице
      l=b[5-1-k]#присваиваем элементы массива b из x элементов в обратном порядке ,и выводим в столбик
      print(l)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break