#Task1 Користувач вводить радіус кола. Потрібно обрахувати
# площу круга та вивести результат з двома знаками після коми.

#Просить користувача ввести дані
# radius = float(input("Введіть радіус кола: "))
# pi = 3.1415

#Знаходить площу
# area = pi * radius ** 2

#Виводить площу кола
# print(f"Площа кола: {area:.2f}")
# print()


#Task2 Користувач вводить ціну однієї кружки та загальний бюджет.
# Виведіть скільки кружок можна купити

#Просить користувача ввести дані
# price_onecup = float(input("Введіть ціну однієї кружки: "))


# budget  = float(input("Введіть бюджет: "))
# user_cups = budget // price_onecup
# print(f"Можна купити: {user_cups} кружки")


#Task3 Користувач вводить довжину в метрах. Виведіть цю
#довжину в футах та ярдах

# #Просить користувача ввести дані
# lenth_meters = float(input("Введіть довжину в метрах: "))
# meters_to_feet = 3.2808399
# meters_to_yards = 1.0936133
#
# #Знаходить довжину у футах
# lenth_feet = lenth_meters*meters_to_feet
#
# #Знаходить довжину у ярдах
# lenth_yards = lenth_meters*meters_to_yards
#
# #Виводить отриману довжину у футах
# print(f"Довжина у футах: {lenth_feet}")
# #Виводить отриману довжину у ярдах
# print(f"Довжина у ярдах: {lenth_yards}")


#Task4 У завданні 2 виведіть ще залишок коштів

# price_onecup = float(input("Введіть ціну однієї кружки: "))
# budget  = float(input("Введіть бюджет: "))
# user_cups = budget // price_onecup
# change = budget % price_onecup
# print(f"Можна купити: {user_cups} кружки")
# print(f"Решта: {change} грн ")


#Task5 Користувач вводить загальну кількість хвилин.
# Переведіть їх у години та хвилини.
# minutes = int(input("Введіть кількість хвилин: "))
# total_hours = minutes // 60
# remain_minutes = minutes % 60
# print(f"Годин: {total_hours}")
# print(f"Хвилин: {remain_minutes}")


#Task6 Щоб спекти пиріг потрібно 4 яблука та 1.2 літра молока.
# Користувач вводить кількість яблук та молока(у літрах).
# Виведіть скільки він може спекти пирогів.
# Виведіть скільки яблук та молока залишиться.


# apples = int(input("Введіть кількість яблук: "))
# milk = float(input("Введіть кількіть молока в літрах: "))
# pie_apples = apples // 4
# pie_milk = int(milk // 1.2)
# pies = min(pie_apples, pie_milk)
# remain_milk = milk - (pies * 1.2)
# remain_apples = apples - pies* 4
# print(f"Зможете спекти пирогів: {pies}  "
#       f"\nЗалишиться яблук: {remain_apples}"
#       f"\nЗалишиться молока: {remain_milk:.2f} л")

#Task7 Користувач вводить суму вкладу в банк та відсоток ставки.
# ● Обчисліть скільки користувач отримує через 5 років,
# якщо кожного року сума вкладу збільшується на даний
# відсоток
# ● Виведіть суму вкладу кожного року окремо


# deposit = float(input("Введіть суму депозиту: "))
# rate = float(input("Введіть відсоток ставки(%): "))
# deposit_first = deposit + (deposit * (rate/100))
# deposit_second = deposit_first + (deposit_first* (rate/100))
# deposit_third = deposit_second + (deposit_second* (rate/100))
# deposit_fourth =  deposit_third + (deposit_third* (rate/100))
# deposit_fifth = deposit_fourth + (deposit_fourth* (rate/100))
# print(f"Перший рік: {deposit_first:1.2f} грн"
#       f"\nДругий рік: {deposit_second:.2f} грн"
#       f"\nТретій рік: {deposit_third:.2f} грн"
#       f"\nЧетвертий рік: {deposit_fourth:.2f} грн"
#       f"\nП'ятий рік: {deposit_fifth:.2f} грн")


#Task8 Користувач вводить кількість днів. Виведіть скільки це років, тижнів та днів.
total_days = int(input("Enter the number of days: "))
years = total_days // 365
remain = total_days % 365
weeks = remain // 7
days = remain % 7
print(f"{total_days} days - {years} year/s, {weeks} week/s, {days} day/s")