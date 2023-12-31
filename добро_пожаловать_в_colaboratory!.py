# -*- coding: utf-8 -*-
"""Добро пожаловать в Colaboratory!

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

# Лабораторная работа 3 Лиманский ИСТ-311
"""

months = {
    1: "Январь",
    2: "Февраль",
    3: "Март",
    4: "Апрель",
    5: "Май",
    6: "Июнь",
    7: "Июль",
    8: "Август",
    9: "Сентябрь",
    10: "Октябрь",
    11: "Ноябрь",
    12: "Декабрь"
}

user_input = int(input())

if user_input in months.keys():
    print(months[user_input])
else:
    print("Такого месяца нет!")

def even_odd(n):
    if n % 2 == 0:
        return "Это четное число"
    else:
        return "Это нечетное число"

n = int(input("Введите любое число: "))
print(even_odd(n))

n = int(input())
if n > 40:
  print("stonks")
else:
  print("not stonks")

import calendar

def is_year_leap(year):
    return calendar.isleap(year)

year = int(input("Enter a year: "))

if is_year_leap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Введите число, для которого нужно проверить, является ли оно простым:"))

if is_prime(num):
    print(num, "является простым числом")
else:
    print(num, "не является простым числом")

def switch_if_condition(a, b):
    if (a >= 3.6 * b or b >= (-138 / (2 ** 1.3)) or b <= -69 / (28 ** 5.1) * 4) and a != b:
        a, b = b, a
    return a, b

a = int(input("Введите a: "))
b = int(input("Введите b: "))
result = switch_if_condition(a, b)
print(result[0], result[1])

def main():
    numbers = [int(x) for x in input("Введите пять чисел через пробел: ").split()]

    def is_unique(nums):
        nums.sort()
        return nums == sorted(nums)

    def count_values(nums, value):
        count = 0
        for num in nums:
            if num == value:
                count += 1
        return count

    print(f"Уникальные числа: {is_unique(numbers)}")
    print(f"Четные числа: {count_values(numbers, 0)}")
    print(f"Отрицательные числа: {count_values(numbers, -1)}")
    print(f"Числа в промежутке: {count_values(numbers, 256)}")

if __name__ == "__main__":
    main()