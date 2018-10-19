import math
import random


# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

num_list = [1, 2, 4, 0]
print([math.pow(x,2) for x in num_list])


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fr1 = ['apple', 'orange', 'pear', 'peach', 'mango', 'banana', 'pineapple']
fr2 = ['lemon', 'banana', 'guava', 'lime', 'orange', 'pomelo']
print([f1 for f1 in fr1 if f1 in fr2])


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

num_list1 = [random.randint(-100,100) for i in range(-100,100)]
print([x for x in num_list1 if x > 0 and x % 3 == 0 and x % 4 != 0])
