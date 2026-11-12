# Task1 - Користувач вводить суму на рахунку в банку та суму
# покупки. Виведіть на екран залишок коштів
# balance = float(input("Введіть суму на рахунку в банку: "))
# purchase = float(input("Введіть суму покупки:"))
# remain_balance = balance - purchase
# print("Залишок: ",remain_balance )


#Task2 -  Напишіть програму яка запитує в користувача ціну однієї чашки кави(може бути з копійками)
# та кількість чашок.

# price = float(input("Яка ціна однієї чашки кави: "))
# amount = int(input("Яка кількість чашок: "))
# general = price*amount
# print("Сума замовлення: ", general)



#Task3 - fix mistakes

# width = int(input("Введіть ширину: "))
# height = int(input("Введіть висоту: "))
# area = width * height
# print("Площа дорівнює:", area)



# #Task4 - Ви обідаєте з друзями в ресторані і вирішуєте скільки залишити чайових.
# Користувач вводить суму рахунку та відсоток чайових(наприклад 10, 15 чи 20).
# Виведіть чайові та загальну суму на окремих рядках з підписами

# bill =  float(input("Введіть суму рахунку: "))
# tips = int(input("Введіть кількість чайових: "))
# general = bill + tips
# print("Рахунок: ", bill)
# print("Чайові: ", tips)
# print("До сплати: ", general)


#Task5 - Потрібно спланувати витрати на поїздку.
# Користувач вводить
# ● відстань в км
# ● витрати пального на 100 км в літрах ● ціна 1 л пального
# Виведіть на екран кількість пального та його ціну

# distance = float(input("Введіть відстань в км: "))
# consumption = float(input("Введіть витрати пального на 100 км в літрах: "))
# price = float( input("Введіть ціну 1 л пального: "))
#
# total_fuel = (distance*consumption)/100
# total_cost = total_fuel*price
# print("Загальна кількість необхідного пального: ", total_fuel)
# print("Загальна вартість пального: ", total_cost)


#Task6 - fix mistakes

# num1 = int(input("перше число: "))
# num2 = int(input("друге число: "))
# result = num1 + num2
# result1 = num1 - num2
# result2 = num1 * num2
# print("Результат 1: ", result, "\nРезультат 2: ", result1, "\nРезультат 2: ", result2)


#Task7 - Ви вирішили покинути ресторан. У завданні 4 модифікуйте код так,
# щоб ще вводилась кількість людей і виводило на екран скільки має заплатити кожен(включно з чайовими)

# bill =  float(input("Введіть суму рахунку: "))
# tips = int(input("Введіть кількість чайових: "))
# persons = int(input("Введіть кількість людей: "))
# general = (bill + tips)/persons
# print("Кількість людей: ", persons)
# print("Кожен має заплатити: ", general)

#Task8
# buyer_money = float(input("Введіть суму грошей покупця: "))
# price = float(input("Введіть вартість товару: "))
# change = buyer_money - price
# print("Здача:", change)

#Task9
user_name = input("Введіть ім'я: ")
user_dateofbirth = int(input("Введіть вашу дату народження: "))
user_height = input("Введіть ваш зріст: ")

age = 2026 - user_dateofbirth

print("\t=== АНКЕТА КОРИСТУВАЧА ===","\nІм'я: ", user_name, "\nВік: ", age,"роки/ів", "\nЗріст: ", user_height, "м")

