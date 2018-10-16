import math


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    def fib(n):
        num_1 = 0
        num_2 = 1
        for _ in range(n):
            num_1, num_2 = num_2, num_1 + num_2
        return num_1
    return [fib(y) for y in range(n,m + 1)]

print(fibonacci(1, 5))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(1, len(origin_list)):
        a = i - 1
        b = origin_list[i]
        while a >= 0 and b < origin_list[a]:
            origin_list[a + 1] = origin_list[a]
            a -= 1
            origin_list[a + 1] = b
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(v, list):
    return[i for i in list if v(i)]

v = lambda i: i / -2 > 0
my_list = [12, 2, 45, -14, 8, 0, -5]

print(my_filter(v, my_list))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def par(A, B, C, D):                                            # Заменил А1 на А, А2 на В, А3 на С, А4 на D, чтобы проще
    AB = math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)     # было разобраться с точками
    BC = math.sqrt((B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2)
    CD = math.sqrt((D[0] - C[0]) ** 2 + (D[1] - C[1]) ** 2)
    AD = math.sqrt((D[0] - A[0]) ** 2 + (D[1] - A[1]) ** 2)
    if AB == CD and BC == AD:
        print('Это параллелограм')
    else:
        print('Это не параллелограмм')

A = (1, 5)
B = (0, 1)
C = (8, 5)
D = (9, 1)

# Является параллелограмом, что и доказывается программой

print(par(A,B,C,D))

