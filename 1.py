#Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
#один рядок через кому. Отримайте для масиву середнє арифметичне.
#Павлюк Владислав 122-В
import numpy as np#импортируем библиотеку нампи
while True:
    b=np.zeros(5,dtype=int)#инициализируем масив нулями,и присваеиваем типу данных тип данных инт
    u=[]#пустой список для выходного масива
    for i in range(5):#проходимся по елементам масива
      b[i] = int(input('Введите ваши элементы: '))#вводим значения
    for k in range(5):#снова проходимся по нашей масиву
      l=b[k]#помещаем элементы в пустую переменную
      u.append(l)#добавляем в список
    print(u)
    g=sum(u)/5#ищем среднее арифметическое
    print('Среднее арифитическое',g)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
