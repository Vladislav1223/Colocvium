#Обчислити суму парних елементів одновимірного масиву до першого
#зустрінутого нульового елемента.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
while True:
    b=np.zeros(5,dtype=int)#инициализируем масив нулями,и присваеиваем типу данных тип данных инт
    count=0
    for i in range(5):#проходимся по елементам масива
      b[i] = int(input('Введите значение'))#вводим значения
    print(b)
    for k in range(5):#снова проходимся по нашему масиву
      if b[k]%2==0:#если элемент парный то сумируем их в наш счетчик,но если переберая значения масива встретится 0,выход из цикла
          if b[k]==0:
              break
          else:
              count+=b[k]
    print(count)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break