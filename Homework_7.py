import random

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""


class Kegs_in_bag:
    def __init__(self):
        self.kegs = [i for i in range(1, 91)]

    def pull_keg_out(self):
        choice = random.choice(self.kegs)
        self.kegs.remove(choice)
        print('Keg: {} (Kegs left {})'.format(choice, len(self.kegs)))
        return choice


class Card:
    def __init__(self, name):
        self.stat = 0
        self.name = name
        self.card = ['' for _ in range(9 * 3)]
        pos = []
        for i in range(3):
            pos.extend(random.sample(range(i * 9, (i + 1) * 9), 5))
        num = random.sample(range(1, 91), 15)
        for i in pos:
            self.card[i] = num.pop(0)

    def card_inf(self):
        print(self.name)
        for i in range(3):
            print('%2s %2s %2s %2s %2s %2s %2s %2s %2s ' % tuple(self.card[i * 9:(i + 1) * 9]))
        print('--------------------------')

    def actions(self, choice, answer=None):
        if answer:
            if answer == 'Y' and choice in self.card:
                self.card[self.card.index(choice)] = 'X'
            elif answer == 'Y' and choice not in self.card:
                self.stat = -1
            elif answer == 'N' and choice not in self.card:
                pass
            elif answer == 'N' and choice in self.card:
                self.stat = -1
            elif answer == 'Q':
                answer1 = input('Are you sure you want to quit? (Y/N)')
                if answer1 == 'Y':
                    exit()
                elif answer1 == 'N':
                    pass
            else:
                print('Try one more time')
                self.stat = -1
        else:
            if choice in self.card:
                self.card[self.card.index(choice)] = '-'
        if (int not in list(map(type, self.card))):
            self.stat = 1


Keg = Kegs_in_bag()
User = Card('========YOUR==CARD========')
Comp = Card('======COMPUTERS=CARD======')
while abs(User.stat) + abs(Comp.stat) == 0:
    choice = Keg.pull_keg_out()
    User.card_inf()
    Comp.card_inf()
    User.actions(choice, input('Do you want to cross the number out? (Y/N):'))
    Comp.actions(choice)

if User.stat == 1:
    if Comp.stat == 1:
        print('=======DRAW=======')
    else:
        print('!!!!!YOU!!WIN!!!!!')
else:
    print('!!!!YOU!!LOOSE!!!!')

