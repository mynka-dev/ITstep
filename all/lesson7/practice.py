#Task1
import time
from asyncio import wait

# amount = int(input("Введіть кількіть печива: "))
# print("Вміст кошика:")
# for cookie in range(amount):
#     print("🍪", end="")

#Task2
# account = int(input("Введіть кількість рахунков: "))
# for num in range(1001,account + 1001):
#     print(f"INTV - {num}")


#Task3
# days = int(input("Раз на скільки днів тренуватися: "))
# for day in range(1, 31, days):
#     print(f"День тренування: {day}")



#Task4

# sweet = input("Що обираєте?\n(🍪 🧁 🍩 🍬 🍫 🍭 🥨 🥠 🍰 🍎 🍏 🍐 🍊 🍌 🍉 🍇 🍓 🫐 🍒 🍑 🥭 🥝): ")
# amount = int(input("Введіть кількіть: "))
# print("Вміст кошика:")
# for sweets in range(amount):
#     print(sweet, end="")


#Task5
# seconds = int(input("Введіть кількість секунд: "))
# for sec in range(seconds,0,-1):
#     time.sleep(1) # знайшов сам
#     print(sec)
# print("Запуск!")


#Task6
# num = int(input("Введіть число: "))
# for sequence in range(1, 11):
#     result = num * sequence
#     print(f"{num} * {sequence} = {result}")


#Task7
# deposit = float(input("Введіть суму депозиту: "))
# rate = float(input("Введіть відсоток ставки(%): "))
#
# for year in range(1,6):
#     deposit *= (1+rate/100)
#     print(f"Рік: {year}"
#           f"\nДепозит: {deposit:.2f} грн")

# Additional tasks:


 #Task1  Користувач вводить з клавіатури два числа.
# Вкажіть усі числа у заданому діапазоні.


# num1 = int(input("Введіть перше число: "))
# num2 = int(input("Введіть друге число: "))
# if num1 > num2:
#     for numbers in range(num1 -1, num2, -1):
#         print(numbers, end= " ")
# else:
#     for numbers in range(num1 + 1, num2):
#         print(numbers, end= " ")


#Task2  Користувач вводить з клавіатури два числа.
# Вкажіть усі непарні числа у заданому діапазоні.
# num1 = int(input("Введіть перше число: "))


# num2 = int(input("Введіть друге число: "))
#
# if num1 > num2:
#     for numbers in range(num1 - 1, num2, -1):
#         if numbers % 2 != 0:
#             print(numbers, end = " ")
# else:
#     for numbers in range(num1 + 1, num2):
#         if numbers % 2 != 0:
#             print(numbers, end = " ")



#Task3    Користувач вводить з клавіатури два числа.
# Вкажіть усі парні числа у заданому діапазоні.


# num1 = int(input("Введіть перше число: "))
# num2 = int(input("Введіть друге число: "))
#
# if num1 > num2:
#     for numbers in range(num1 - 1, num2, -1):
#         if numbers % 2 == 0:
#             print(numbers, end = " ")
# else:
#     for numbers in range(num1 + 1, num2):
#         if numbers % 2 == 0:
#             print(numbers, end = " ")


#Task4 Користувач вводить з клавіатури два числа.
# Вкажіть усі числа у заданому діапазоні за спаданням.

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

high = max(num1, num2)
low = min(num1, num2)

for numbers in range(high - 1, low + 1 , -1):
    print(numbers,end = " ")

