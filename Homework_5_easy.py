import os
import shutil
import sys
import psutil

#Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def create_dirs():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), "dir_{}".format(i))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print("Folder {} already exists".format(path))
    return "Folders were created."

def remove_dirs():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), "dir_{}".format(i))
        os.rmdir(path)
    return "Folders were deleted."

# Функции для normal

def create_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(path)
        return "Folder was created."
    except FileExistsError:
        return "Folder with this name already exists"

def remove_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    if os.path.isdir(path):
        os.rmdir(path)
        return "Folder was deleted."
    else:
        return "Eror"


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def dir_folders():
    print("Files and folders in current directory:")
    fil_and_fold = os.listdir(path=".")
    for i in fil_and_fold:
        print(i)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def dupl_file():
    copy_filename = __file__ + ".copy"
    shutil.copyfile(__file__, copy_filename)

def change_dir(dir_name):
    try:
        os.chdir(dir_name)
    except FileNotFoundError:
        print(dir_name + ' - Not Found')