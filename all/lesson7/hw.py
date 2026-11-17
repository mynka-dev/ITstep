# Task1  Потрібно порахувати суму чисел в діапазоні,
# але програма виводить не те що треба(загальна сума має бути 15), виправіть помилку

# total = 0
# for number in range(1, 6):
#     total += number
#
# print(f"Сума: {total}")


# Task2

# start = int(input("Введіть перше число: "))
# stop = int(input("Введіть друге число: "))
# minimum = min(start, stop)
# maximum = max(start, stop)
# for num in range(minimum, maximum + 1):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")

#     elif num % 3 == 0:
#         print("Fizz")

#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)


# Task3  Напишіть програму яка протягом 5 робочих днів запитує в кур’єра кількість доставлених замовлень за кожен день.
# В кінці виведіть загальну кількість доставок за робочий тиждень та чи виконано тижневу норму в 50 доставок


total = 0
for days in range(1, 6):
    deliveries = int(input(f"Введіть кількість доставок за день {days}: "))
    total += deliveries
print(f"Загальна кількість доставок за тиждень: {total}")

if total > 50:
    print("Тижневу норму виконано")
else:
    print("Тижневу норму не виконано")
