""" Игра угадай число"""
import numpy as np
number=np.random.randint(0, 101)
print(number)
count = 0
while True:
    count+=1
    predict_number=int(input('Угадай число если не лох с 1 попытки:' ))
    if predict_number<number:
        print("число должно быть больше")
    elif  predict_number>number:
        print("число должно быть меньше")
    else:
        print('Ура!!!', count)
        break