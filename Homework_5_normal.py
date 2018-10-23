import Homework_5_easy


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"
# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

a = ''
while True:
    print("Choose action:\n\
1. Move to a folder\n\
2. Show folders the of current directory\n\
3. Delete folder\n\
4. Create folder")
    break

a = input("Choose (1/2/3/4): ")

if a == '1':
    dir_name = input("Enter name of dir")
    print(Homework_5_easy.change_dir(dir_name))
elif a == '2':
    Homework_5_easy.dir_folders()
elif a == '3':
    dir_name = input("Enter the name of directory")
    print(Homework_5_easy.remove_dir(dir_name))
elif a == '4':
    dir_name = input("Enter the name of directory")
    print(Homework_5_easy.create_dir(dir_name))
else:
    print("Try again.")