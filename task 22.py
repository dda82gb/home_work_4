# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов
# второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint
print("\033[31m\0")
x_set = set(randint(1,10) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(x_set)
print("\033[32m\0")
y_set = set(randint(1,10) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(y_set)
sum_set = sorted(x_set.intersection(y_set))
print("\033[33m\0")
print('Числo(а) которые встречаются в обоих наборах: ')   
print([*sum_set])

