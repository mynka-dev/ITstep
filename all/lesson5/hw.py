#Task1  Користувач вводить ціну за одиницю товару та кількість товару. Я
# кщо загальна сума більша за 500грн або купівля оптом(більше 10 шт), застосувати знижку 10%

# price = float(input("Введіть ціну за одиницю товару: "))
# amount = int(input("Введіть кількість товару: "))
# total = price * amount
# if total > 500 or amount > 10:
#     discount = total - ((total * 10) / 100)
#     print(f"До сплати: {discount} грн")
# else:
#     print(f"До сплати: {total}")
#
#
# print()
# print()


#Task2

day = input("Введіть день тижня: ")
if day == "субота" or day == "неділя":
    print("Вихідний")
else:
    print("Робочий день")


#Task3

question = input("Ало! Котра година: ")
if question == "9":
    print(10)
elif question == "10" or question == "да":
    print("да")
elif question == "":
    print("10!!!")
else:
    print("Ой не чує баба глуха як тетеря")