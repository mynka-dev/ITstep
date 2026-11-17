# Task1 Користувач вводить 2 числа, потрібно вивести середнє арифметичне.Але програма не працює

# num1 = float(input("перше число: "))
# num2 = float(input("друге число: "))
# sum = num1 + num2
# average = sum / 2
# print("Сума:", sum)
# print("Середнє:", average)

# Task2

# sum = float(input("Введіть суму в гривнях: "))
# rate = float(input("Введіть курс долара: "))
# usd = sum/rate
# print("Сума в доларах: ", usd)


# Task3
# price = float(input("Введіть ціну товару: "))
# disc_percentage = int(input("Введіть відсоток знижки: "))
# total_discount = (price/100)*disc_percentage
# print("Сума знижки: ", total_discount)

# Task4
slow_walk_time = float(input("Введіть час повільної ходьби (хв): "))
fast_walk_time = float(input("Введіть час швидкої ходби (хв): "))
run_time = float(input("Введіть час бігу (хв): "))

caloriesfduring_slow = slow_walk_time * 3
caloriesfduring_fast = fast_walk_time * 4.5
caloriesfduring_run = run_time * 9


print("Спалені калорії: ")
print("\tПовільна ходьба - ", caloriesfduring_slow, "ккал")
print("\tШвидка ходьба - ", caloriesfduring_fast, "ккал")
print("\tБіг - ", caloriesfduring_run, "ккал")
