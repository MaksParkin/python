# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class person:
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_fullname(self):
        fullname = self.name + ' ' + self.patronymic + ' ' + self.surname
        return fullname

class student(person):
    def __init__(self, name, surname, patronymic, classroom, parents):
        person.__init__(self, name, surname, patronymic)
        self.classroom = classroom
        self.parents = parents
class teacher(person):
    def __init__(self, name, surname, patronymic, subject):
        person.__init__(self, name, surname, patronymic)
        self.subject = subject
class classroom:
    def __init__(self, classroom, teachers):
        self.classroom = classroom
        self.teachers = teachers
teachers = [teacher('Вера', 'Ремизова', 'Леонидовна', 'русский язык'), teacher('Татьяна', 'Иванова', 'Викторовна', 'обществознание')]

classrooms = [classroom('8 a', [teachers[0], teachers[1]]), classroom('8 б', [teachers[0]])]
parents = [person('Валентин', 'Сидоров', 'Алексеевич'), person('Александр', 'Потемкин', 'Игоревич'),person('Мария', 'Сидорова', 'Васильевна'),
           person('Екатерина', 'Потемкина', 'Максимовна')]
students = [student('Леонид', 'Сидоров', 'Валентинович', classrooms[0], [parents[0], parents[2]]),
            student('Георгий', 'Потемкин', 'Александрович', classrooms[1], [parents[1], parents[3]])]

print("Классы:")
for cl in classrooms:
    print(cl.classroom)

which_classroom = '8 б'
print("Ученики {}:".format(which_classroom))
for i in students:
    if i.classroom.classroom == which_classroom:
        print(i.get_fullname())

w_student = 'Леонид Сидоров'
print("Предметы {}:".format(w_student))
for i in students:
    if i.surname == w_student.split()[1] and i.name == w_student.split()[0]:
        for teacher in i.classroom.teachers:
            print(teacher.subject)

which_student = 'Леонид Сидоров'
print("ФИО родителей {}:".format(which_student))
for i in students:
    if i.surname == w_student.split()[1] and i.name == w_student.split()[0]:
        for parent in i.parents:
            print(parent.get_fullname())

w_classroom = '8 б'
print("Учителя {}:".format(which_classroom))
for n in classrooms:
    if n.classroom == w_classroom:
        for teacher in n.teachers:
            print(teacher.get_fullname())