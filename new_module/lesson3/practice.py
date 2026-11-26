# Task1


# numbers = [1, 8, -5, 9]
# print(numbers)
# for number in range(len(numbers)):
#     numbers[number] *= 3
# print(numbers)
#
#
# for number1 in range(len(numbers)):
#     if numbers[number1] > 10:
#         numbers[number1] = 0
# print(numbers)


# Task2


# numbers = []
# number = int(input("Введіть число: "))
# while number != -1:
#     number = int(input("Введіть число: "))
#     if number != -1:
#         numbers.append(number)
#     if number == -1:
#         print(f"Кількість - {numbers}\n"
#               f"Сума - {sum(numbers)}\n"
#               f"Мінімальне - {min(numbers)}\n"
#               f"Максимальне - {max(numbers)}\n")


# Task3

# positive = []
# negative = []
#
# while True:
#     number = int(input("Введіть число (0 для завершення): "))
#
#
#     if number == 0:
#         break
#
#     elif number > 0:
#         positive.append(number)
#         continue
#
#     else:
#         negative.append(number)
#         continue
#
# print("Додатні числа:", positive)
# print("Від'ємні числа:", negative)


# Task4
# worker_num = int(input("Введіть кількість робітників:"))
# salaries = []
#
# for i in range(worker_num):
#     salary = float(input(f"Введіть зарпалату робітника {i + 1}: "))
#     salaries.append(salary)
# percent = float(input("На який відсоток збільшити: "))
#
# new_salaries = []
# for salary in salaries:
#     new_salary = round(salary * (1 + percent / 100), 2)
#     new_salaries.append(new_salary)
#
# print("Нові зарплати:", new_salaries)


# Task5


days = int(input("Введіть кількість днів: "))
temperatures = []
for i in range(days):
    temperature = float(input(f"Введіть температуру за {i + 1}-й день: "))
    temperatures.append(temperature)

print("Температури:", temperatures)

for i in range(1, days):
    difference = temperatures[i] - temperatures[i - 1]
    print(f"Різниця температур за {i + 1}-й день: {difference}")
