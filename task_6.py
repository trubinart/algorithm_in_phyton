"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

#счетчик попыток
import random
number = random.randint(0,100)

def guess(number = random.randint(0,100), count=0, asc=0):
    if count > 10:
        return print(f'Вы не отгадали число. Правильное число {number}.')

    if count <= 10:
        if asc != number:
            print(number)
            asc = int(input('Порпобуйте отгадать число: '))
            guess(number, count + 1, asc)
        else:
            return print(f'Молодец! Отгадал число {number}')

guess()