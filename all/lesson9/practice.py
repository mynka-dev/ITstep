#Task1  Користувач вводить число від 1 до 9. Потрібно вивести для цього числа таблицю множення.
# Якщо користувач ввів неправильне число то продовжувати запитувати поки не введе правильне.
import random
# while True:
#     num = int(input("Введіть число від 1 до 9: "))
#     if num < 0 or num > 9:
#         print("Неправильний ввід")
#         print()
#         continue
#     else:
#         break
#
# for multiply in range(1,11):
#     multiplication = multiply * num
#     print(f"{num}x{multiply} = {multiplication}")

#Task2

# total = 0
# count = 0
# while True:
#     grade = int(input("Введіть оцінку: "))
#     if grade == 0:
#         break
#
#     count += 1
#     total += grade
#
#
# average_grade = total / count
# print(f"середня оцінка: {average_grade:.2f}")

#Task3


# while True:
#     num1 = int(input("Введіть перше число: "))
#     num2 = int(input("Введіть друге число: "))
#     print("\nОберіть дію, яку хочете виконати:")
#     print("1. Сума\n2. Різниця\n3. Добуток\n4. Частка\n5. Вихід")
#
#     user_action = int(input("Ваш вибір: "))
#     if user_action == 5:
#         break
#     elif user_action == 4:
#         if num2 == 0 or num1 == 0:
#             print("На нуль ділити неможна")
#             print()
#             continue
#         action = num1 / num2
#
#     elif user_action == 3:
#         action = num1 * num2
#
#     elif user_action == 2:
#         action = num1 - num2
#
#     elif user_action == 1:
#         action = num1 + num2
#
#     else:
#         print("Некоректний вибір, спробуйте ще раз.")
#     print(f"Результат - {action}")


#Task4

# for i in range(1,4):
#     name = input("Введіть ім'я: ")
#     while name == "admin":
#         print("Це ім'я недоступне")
#         name = input("Введіть ім'я: ")
#         continue
#
#     print(f"Учасник №{i}: {name}")


#Task5
tries = 0
secret_num = random.randint(0, 100)
while True:
    num = input("Введіть число: ")
    tries += 1
    if num == "stop":
        print(f"Спроб: {tries} Загадане число - {secret_num}")
        break
    num = int(num)
    if num > secret_num:
        print("Забагато")
    elif num < secret_num:
        print("Замало")
    else:
        print(f"Вітаю! Ви вгадали\nСпроб - {tries}")
        break