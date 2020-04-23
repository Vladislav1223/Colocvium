#45. Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
#яка містить довжини опор, які встановлюються через кожні R / 5 м.
#Павлюк владислав
import math
while True:
    R=int(input('Введите радиус: '))
    diametr=2*R #Ищем наш диаметр

    R1=R/5 #значение опоры каждые 5 метров
    count=0
    number=0 #Номер опоры

    while count<diametr-R1:#Пока значение нашего счетчика меньше длинны диаметра -опоры
        count+=R1
        number+=1
        print('Номер опoры',number, math.sqrt(count*(diametr-count)))
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
