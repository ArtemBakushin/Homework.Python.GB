def filling_the_array (n,m,c):
    list_1=list()
    for i in range(n,c*m+n,c):
        list_1.append(i)
        i+=1
    return list_1
    print(list_1)
    

n=int(input('Ввидети число откуда начинать счет: '))
c = int(input('Введите шаг: ')) 
m= int(input('Размер массива: '))

print(filling_the_array(n,m,c))



