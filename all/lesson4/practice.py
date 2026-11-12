#Task1 Користувач вводить час у хвилинах, виведіть скільки це
# секунд. Якщо введено від’ємне число виведіть
# повідомлення “Час має бути додатнім”
#
# minutes = float(input("Введіть час у хвилинах: "))
# if minutes>= 0:
#     seconds = int(minutes*60)
#     print(f"{minutes} хвилин = {seconds} секунд")
# else:
#     print("Час має бути додатнім")


# print()
# print()
#Task2  Напишіть програму для перевірки правильності паролю.

# type_password = input("Введіть пароль: ")
# secret_password = "OpenSesame123"
# if type_password != secret_password:
#     print("Доступ заблоковано")
# else:
#     print("Доступ дозволено")

# print()
# print()


#Task3  Користувач вводить довжину в метрах та в що їх
# перевести(сантиметри(см) чи кілометри(км))

# meters = float(input("Введіть довжину в метрах: "))
# question = input("У що перевести, см чи км?: ")
# if question == "см":
#     centimeters = int(meters * 100)
#     print(f"{meters} метрів = {centimeters} сантиметрів")
# elif question == "км":
#     kilometers = meters / 1000
#     print(f"{meters} метрів = {kilometers} кілометрів")
# else:
#     print("Помилка у віповіді! Введіть коректно, см або км")

# print()
# print()

#Task4  Напишіть програму яка перевірить чи правильно дано
# відповідь на Велике Питання Життя, Всесвіту і Всього
# Іншого.
# Просить ввести користувача відповідь
# question2 = input("Введіть відповідь на Велике Питання Життя, Всесвіту і Всього Іншого: ")
#Порівння відповіді юзера з правильною
# if question2 == "42":
#     print("Відповідь правильна")
# elif question2 == "сорок два":
#     print("Відповідь правильна")
# elif question2 == "сорок-два":
#     print("Відповідь правильна")
#Якщо ні одна версія не співпала, то означає що юзер помилився і спрацює else
# else:
#     print("Відповідь неправильна \nСпробуй ще!")


#Task5

# grade = int(input("Введіть вашу оцінку: "))
#
# if grade == 2:
#     print("Незадовільно")
# elif grade == 3:
#     print("Задовільно")
# elif grade == 4:
#     print("Добре")
# elif grade == 5:
#     print("Відмінно")
# else:
#     print("Має бути між 2 та 5")

# print()
# print()



#Task6    Ви плануєте замовити піцу для компанії людей.
# Користувач вводить ціну однієї піци, кількість піц та
# ваш загальний бюджет.
# Перевірте чи вистачає вам грошей. Якщо ні то виведіть
# скільки саме не вистачає

# pizza_price = float(input("Введіть ціну однієї піцци: "))
# pizza_amount = int(input("Введіть кількість піц: "))
# buget = float(input("Введіть ваш бюджет: "))
#
# price = pizza_amount*pizza_price
#
# if price > buget:
#     not_enought = price - buget
#     print(f"Вам не вистачає {not_enought} гривень")
# else:
#     pizzas = int(buget // price)
#     print(f"Вам вистачає на {pizzas} піцц")

# print()
# print()


# Task7  Користувач вводить з клавіатури число. Необхідно перевірити його на парність і непарність.
# Якщо число парне потрібно вивести на екран число і напис "Even number".
# Якщо число непарне виведіть на екран число і напис "Odd number".


# number = int(input("Type the number: "))
# even_number = number % 2
# if even_number == 0 :
#     print("This number is even")
# else:
#     print("This number is odd")

# print()
# print()


# Task8
# Користувач вводить із клавіатури число. Необхідно перевірити його на кратність 7.

# number = int(input("Type the number: "))
# multiple_to7 = number % 7
# if multiple_to7 == 0 :
#     print("Number is multiple 7")
# else:
#     print("Number is not multiple 7")

# print()
# print()

# #Task9 Користувач вводить з клавіатури два числа.
# Необхідно знайти максимум з двох чисел і показати його на екран.


# num1 = float(input("Введіть перше число: "))
# num2 = float(input("Введіть друге число: "))
#
# if num1 > num2:
#     print(f"Максимальне число: {num1}")
# elif num2 > num1:
#     print(f"Максимальне число: {num2}")
# else:
#     print("Числа рівні між собою")
#
#
#           # 2 варіант
#
# maxsimum = max(num1,num2)
# print(f"Максимальне число: {maxsimum}")

# print()
# print()

#Task10 Користувач вводить з клавіатури два числа.
# Необхідно знайти максимум з двох чисел і показати його на екран.
# num3 = float(input("Введіть перше число: "))
# num4 = float(input("Введіть друге число: "))
#
# if num3 > num4:
#     print(f"Мінімальне число: {num4}")
# elif num4 > num3:
#     print(f"Мінімальне число: {num3}")
# else:
#     print("Числа рівні між собою")
#
#
#           # 2 варіант
#
# minimum = min(num3,num4)
# print(f"Мінімальне число: {minimum}")


# Task11Користувач вводить з клавіатури два числа.
# Залежно від вибору користувача потрібно показати суму двох чисел, різницю двох чисел,
# середньоарифметичне або добуток двох чисел.

num5 = float(input("Введіть перше число: "))
num6 = float(input("Введіть друге число: "))
question_to_user = ("Введіть:\t\t \"sum\""", якщо хочете порахувати суму цих чисел\n"
                  "\"difference\", якщо хочете порахувати різницю цих чисел\n"
                  "\"average\", якщо хочете порахувати середньоарифметичне\n"
                  "\"product\", якщо хочете порахувати добуток\n")
print(question_to_user)
question3 = input("Що обираете?: ")
if question3 == "sum":
    sum = num5 + num6
    print(f"Сума цих чисел: {sum}")
elif question3 == "difference":
    difference = num5 - num6
    print(f"Різниця цих чисел: {difference}")
elif question3 == "average":
    average = (num5 + num6) //2
    print(f"Середньоарифметичне цих чисел: {average}")
elif question3 == "product":
    product = num5*num6
    print(f"Добуток цих чисел: {product}")
else:
    print("Ви ввели некоректний запит!")