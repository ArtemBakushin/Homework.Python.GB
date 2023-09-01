# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
first_list = list()
second_list = list()
firstPlenty = set()
secondPlenty = set()
intrsct = set()
otvet=list()

for i in range(n:=int(input('Введите кол-во элементов первого множества: '))):
    if (l:=int(input(f'Введите {i+1} элемент первого множества '))) < 10000:
        first_list.append(l)
        
for i in range(m:=int(input('Введите кол-во элементов второго множества: '))):
    if (f:=int(input(f'Введите {i+1} элемент второго множества '))) < 10000:
        second_list.append(f)

firstPlenty=set(first_list)
secondPlenty=set(second_list)
intrsct = firstPlenty.intersection(secondPlenty)
otvet=list(intrsct)
otvet2=sorted(otvet)

print(n)
print(m)
print(*first_list)
print(*second_list)
print(*otvet2)








       

    

# print(f'{b}')
# while (l:= int(input(f'Введите {m} элементов второго множества'))) in range(m+1):
#     c.add(l)
#     print(f'{c}')
