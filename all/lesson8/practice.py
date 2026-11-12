# Task1 Користувач вводить свої ім’я та вік. Якщо введено від’ємне число то попросити ще раз ввести правильний вік поки не буде введено додатнє число.
# В кінці вивести привітання “Привіт Джон. Тобі 36 років”


# name = input("Введіть ім'я: ")
# age = int(input("Введіть вік: "))

# while age < 0 :
#     age = int(input("Введіть правильний вік: "))

# print(f"Привіт {name}. Тобі {age} років")


#Task2  Виправте помилку в коді


# total = 0
# goal = float(input("Цільова сума? "))
#
# while True:
#     daily_amount = float(input("Сьогоднішній вклад? "))
#     total += daily_amount
#     if total >= goal:
#         break
#
# print(f"Мету досягнуто! У скарбничці {total} грн.")


#Task3  Користувач вводить довжину в метрах. Покажіть її у
# ● Ярдах(1 ярд = 0,9144 метра)
# ● Футах(1 фут = 0,3048 метра)
# В кінці спитайте користувача чи продовжувати роботу
# програми.


# while True:
#     meters = float(input("Введіть довжину в метрах: "))
#
#     yard = meters * 0.9144
#     feet = meters * 0.3048
#
#     print(f"Метри в ярдах: {yard}"
#           f"\nМетри в футаз: {feet}")
#
#     question = input("Продовжувати роботу?: ")
#
#     if question == "ні":
#         break


#Task4  У завданні 2 ще виведіть кількість днів за яку була зібрана потрібна сума.


# goal = float(input("Цільова сума? "))
#
# total = 0
# days = 0
# while True:
#     daily_amount = float(input("Сьогоднішній вклад? "))
#
#     total += daily_amount
#     days += 1
#
#     if total >= goal:
#         break
#
# print(f"Мету досягнуто за {days} дні! У скарбничці {total} грн.")


#Task5  Ваш колега написав програму для підрахунку кількість товарів, але програма не виводить фразу
# Підрахунок завершений , виправте помилку


# total_items = 0
# print("Додайте товари. Для завершення введіть 'stop'.")
#
# while True:
#     item = input("Введіть товар: ")
#
#
#
#     if item == "stop":
#         print("Підрахунок завершений")
#         break
#     total_items += 1
#
# print(f"Всього товарів додано: {total_items}")



#Task6  Напишіть програму для введення пароля від банкомату.
# У користувача є лише три спроби
# В кінці виведіть чи вдалось правильно ввести пароль


# password = 1256
# attempts = 0
# while True:
#         password_check = int(input("Введіть пароль: "))

#         attempts += 1

#         if password == password_check:
#             print("Пароль введено правильно!")
#             break

#         else:
#             remaining = 3 - attempts
#             print(f"У вас залишилось {remaining} спроб")
#
#             if attempts == 3:
#                 print("Спроби закінчилися!")
#                 break


