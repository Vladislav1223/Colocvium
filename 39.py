#Дані про температуру повітря і кількості опадів за декаду квітня
#зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
#вигляді снігу за цю декаду.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
import random
while True:
    b=np.zeros(10,dtype=int)#инициализируем  масив нулями,и присваиваем типу данных тип данных инт
    a=np.zeros(10,dtype=int)
    for i in range(10):#проходимся по елементам матрицы
      b[i] = random.randint(-5,5) #Температура воздуха
      a[i]=random.randint(0,10)# осадки
    print('Температура',b)
    print('Осадки мм',a)
    count=0
    opad_sneg=0
    opad_dojd=0
    vse_osad=0
    for k in range(10):
          if b[k]<0:#Ищем элементы температуры ниже нуля,их сумируем элементы по соответвующим индексам в масиве с осадками
              opad_sneg+=a[k]
    for o in range(10):
        vse_osad+=a[o]#Ищем общее число осадков,и вычитаем из них снежные осадки
        opad_dojd=vse_osad-opad_sneg
    print('Количество снежных осадков',opad_sneg,'Дождевые осадки',opad_dojd)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
