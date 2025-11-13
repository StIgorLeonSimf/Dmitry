"""
Написать функцию деления случайных чисел с задержкой в пол секунды.
Навесить на неё декоратор который в текстовый файл пропишет лог
дата время - деление на ноль
"""
import datetime
import random
import time


def decor(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except ZeroDivisionError:
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(f'{datetime.datetime.now().replace(microsecond=0)}'
                        f' - деление на ноль\n')
            return 'Деление на ноль'
    return wrapper


@decor
def div():
    time.sleep(1)
    x = random.randint(0, 50)
    y = random.randint(0, 4)
    return x / y


for _ in range(10):
    print(div())