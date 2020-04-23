#Розсортуйте заданий лінійний масив по зростанню.
#Павлюк Владислав
import numpy as np
import random
while True:
  x=int(input('Введите количество цифр '))
  A=np.zeros(x,dtype=int) #Заводим масив,и заполняем его рандомными значениями
  for i in range(x):
   A[i]=random.randint(0,100000)
  print(A)
  n=len(A)
  for i in range(1,n): #Сделаем сортировку пузырьковым методом
      for j in range(n-1,i-1,-1):
            if (A[j-1]>A[j]):
                A[j],A[j-1]=A[j-1],A[j]
  print(A)
  result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
  if result == '1':
        continue
  else:
        break
