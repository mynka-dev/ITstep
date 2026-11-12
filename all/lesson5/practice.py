#Task1  Користувач вводить свій вік, якщо він працездатного
# віку(18-65) то виведіть фразу «Працездатний/на», інакше
# «Непрацездатний/на»


# age = int(input("Введіть свій вік : "))
# if 18 <= age <= 65:
#     print("Працездатний/на")
# else:
#     print("Непрацездатний/на")

# print()
# print()


#Task2  До завдання 2 з попереднього заняття добавте додаткову
# перевірку: щоб отримати доступ користувач повинен ще й
# ввести правильний логін secret_login = "AliBaba"


# type_password = input("Введіть пароль: ")
# type_login = input("Введіть логін: ")
# secret_password = "OpenSesame123"
# secret_login = "AliBaba"
# if type_password == secret_password and type_login == secret_login:
#     print("Доступ дозволено")
# else:
#     print("Доступ заблоковано")

# print()
# print()



#Task3  Оформіть чек покупки. Користувач вводить ціну за
# одиницю товару, кількість товару та свій вік.
# Якщо користувач неповнолітній або старший за 65
# років, то застосуйте знижку 15%

# price = float(input("Введіть ціну за одиницю товару: "))
# quantity = int(input("Введіть кількість товару: "))
# age = int(input("Введіть ваш вік: "))
# sum = price * quantity
# if 18 <= age <= 65:
#     total = sum - ((sum * 15)/ 100)
#     print(f"До сплати {total} грн")
# else:
#     print(f"До сплати {sum} грн")


# print()
# print()

#Task4 Орендувати авто можна лише якщо
# ● у вас є ліцензія
# ● ви повнолітні
# ● ви не потрапляли в дтп
# Оцініть якість написаного коду, спробуйте його
# спростити використавши and\or


# age = 23
# has_license = "так"
# accidents = 0
# if age >= 18 and accidents == 0 and has_license == "так":
#     print("Оренда дозволена")
# else:
#     print("Оренда заборонена")
#
# print()
# print()


#Task5 Напишіть програму яка запитує у користувача ціну
# покупки та виводить загальну вартість(покупки + доставка)
# Базова ціна доставки: 120 грн
# Знижка діє лише на доставку


# purchase_price = float(input("Введіть ціну покупки: "))
# delivery_price = 120
# if purchase_price < 500:
#     price = purchase_price + delivery_price
#     print(f"До сплати: {price}")
# elif 500 < purchase_price < 1000:
#     discount = purchase_price + (delivery_price - ((delivery_price * 5)/ 100))
#     print(f"До сплати: {discount}")
# elif 1000 < purchase_price < 2000:
#     discount2 = purchase_price + (delivery_price - ((delivery_price * 20)/ 100))
#     print(f"До сплати: {discount2}")
# else:
#     print(f"До сплати: {purchase_price}")

# print()
# print()


#Task6  Користувач вводить суму кредиту та термін у роках.
# Виведіть відсоткову ставку, загальну суму кредиту та  щомісячний платіж


credit = float(input("Введіть суму кредиту($): "))
term = float(input("Введіть термін у роках: "))
if credit < 10000 and term < 3:
    percent = 8
elif  credit < 10000 and term > 3:
    percent = 10
elif 10001 < credit < 50000 and term < 3:
    percent = 12
elif 10001 < credit < 50000 and term >= 3:
    percent = 14
else:
    percent = 20
total = credit * ((1 + percent / 100)**term)
monthly_payment = total / 12
print(f"Ваша відсоткова ставка: {percent}%"
      f"\nЗагальна сума кредиту: {total:.2f}$"
      f"\nЩомісячний платіж: {monthly_payment:.2f}$")
