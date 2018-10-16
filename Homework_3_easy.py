# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = str(number)
    l_digit = int(number[(ndigits + 1)])
    if l_digit >= 5:
        number_out = float(number[0:(ndigits + 1)]) + (0.1 ** (ndigits - 1))
        number_out = str(number_out)
        number_out = float(number_out[0:ndigits + 1])
    else:
        number_out = number[0:(ndigits + 1)]
    return number_out

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    ticket_number_len = len(ticket_number)
    middle = int(ticket_number_len / 2)
    sum_half1 = 0
    sum_half2 = 0
    if ticket_number_len % 2 == 0:
        half1_numbers = list(map(int, list(ticket_number[ :middle])))
        half2_numbers = list(map(int, list(ticket_number[middle: ])))
        for i in half1_numbers:
            sum_half1 = sum_half1 + i
            i += 1
        for i in half2_numbers:
            sum_half2 = sum_half2 + i
            i += 1
    else:
        half1_numbers = list(map(int, list(ticket_number[ :middle])))
        half2_numbers = list(map(int, list(ticket_number[middle + 1: ])))
        for i in half1_numbers:
            sum_half1 = sum_half1 + i
            i += 1
        for i in half2_numbers:
            sum_half2 = sum_half2 + i
            i += 1
    return bool(sum_half1 == sum_half2)

print(lucky_ticket(123006))
