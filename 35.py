#Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
#спаданню.
#Павлюк Владислав
import numpy as np#импортируем библиотеку нампи
while True:
    b=np.zeros(5,dtype=int)#инициализируем матрицу нулями,и присваиваем типу данных тип данных инт
    u=[]
    for i in range(5):#проходимся по елементам матрицы
      b[i] = int(input(''))
      u.append(b[i])  #Добавляем наш масив в список и сортируем его по убыванию
      u.sort(reverse=True)
    print(b)
    print('Отсортированый по убыванию масив',u)
    t=False
    for k in range(5):
        if u[k]!=b[k]:# Проверяем упорядоченость масива,если элементы масива не равны между собой с упорядоченым списком           
          t=False # Т приймет значение ложь,и выйдет из цикла 
          break
        else:
          t=True
    print(t) 
         
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
