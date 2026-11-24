# Task1  Користувач вводить рядок та символ.
# Порахуйте скільки разів цей символ зустрічається у рядку.
# Зробіть двома способами:  ● з методом count  ● з циклом for

# text = input("Введіть текст для перевірки: ")
# symbol = input("Введіть символ: ")
# count = text.count(symbol)
# print(f"{symbol} в '{text}' = {count} ")


# text = input("Введіть текст для перевірки: ")
# symbol = input("Введіть символ: ")
# count = 0
# for ch in text:
#     if ch == symbol:
#         count += 1
#
# print(f"{symbol} в '{text}' = {count} ")


# Task2  Користувач вводить рядок.
# Виведіть наступну інформацію:
# ● кількість символів
# ● чи є там слово python
# ● кількість шиплячих літер – szh


# text = input("Введіть текст для перевірки: ")
#
# count = len(text)
#
# if "python" in text.lower():
#     print("'python' є")
# else:
#     print("'python' немає")
#
# szh_count = 0
# for ch in text.lower():
#     if ch in "szh":
#         szh_count += 1
#
#
# print(f"Кількість символів: {count}")
# print(f"Кількість шиплячих: {szh_count}")


# Task3   Користувач вводить тест. Потрібно замінити всі пробіли на дефіси.
# Виправіть помилку в коді

# text = input("Введіть текст: ")
#
# result = text.replace(" ", "-")
# print(f"Змінений текст: {result}")


# Task4


# text = input("Введіть текст для перевірки: ")
# word = input("Введіть слово: ")
#
# count = text.count(word)
# print(f"{word} в реченні '{text}' = {count}")


# Task5
#
# items = input("Введіть ваші речі: ")
# items = items.lower()
#
# forbidden = ["ніж", "гроші", "отрута"]
#
# has_forbidden = False
# for word in forbidden:
#     if word in items:
#         has_forbidden = True
#         break
#
# if has_forbidden:
#     print("У вас є речі які заборонено перевозити")
# else:
#     print("Оформлено доставку")


# Task6  Користувач вводить текст.
# Порахуйте скільки в ньому літер та цифр.
#
# text = input("Введіть текст для перевірки: ").lower()
#
# digits = 0
# letters = 0
# for ch in text:
#     if ch.isdigit():
#         digits += 1
#     elif ch.isalpha():
#         letters += 1
#
# print("Літер: ", letters)
# print("Цифр: ", digits)


# Task7 Користувач вводить пароль поки не введе його правильно.
# Правильний пароль повинен:
# ● Бути довшим за 8 символів
# ● Містити хоча б одну цифру
# ● Містити хоча б одну літеру


while True:
    password = input("Придумайте пароль: ").lower()

    has_digits = False
    has_numbers = False

    for ch in password:
        if ch.isdigit():
            has_digits = True
        elif ch.isalpha():
            has_numbers = True

    if not has_digits:
        print("Пароль повинен містити хоча б одну літеру ")

    elif not has_numbers:
        print("Пароль повинен містити хоча б одну цифру ")

    elif len(password) <= 8:
        print("Пароль має бути довшим за 8 символів ")

    else:
        print("Пароль прийнято")
        break
