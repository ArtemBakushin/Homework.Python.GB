# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
def Ranges (list_1,n,m):
    list_2 = list()
    for i in range (len(list_1)):   
        if  1+m >list_1[i]>n-1:
            list_2.append(i)
        else:
            i+=1
    return list_2
    

        
from random import randint


list_1 = [randint(1,100) for i in range(int(input('Введите кол-во элементов:')))]
print(list_1)
n = int(input('Введите начало диапозона: '))
m = int(input('Введите конец диапозона: '))
print(Ranges(list_1,n,m))