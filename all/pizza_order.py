print("\033[1mВітаємо вас у нашій піцерії\033[0m")


def print_menu():
    width = 30
    print("╔" + "═" * width + "╗")
    print(f"║{'МЕНЮ':^{width}}║")
    print("╠" + "═" * width + "╣")
    print(f"║ {'1. Маргарита     -  150грн':<{width - 1}}║")
    print(f"║ {'2. Пепероні      -  180грн':<{width - 1}}║")
    print(f"║ {'3. Чотири сири   -  200грн':<{width - 1}}║")
    print("╚" + "═" * width + "╝")


MARHARYTA = 150
PEPERONI = 180
CHOTYRY_SYRY = 200

marharyta_amount = 0
peperoni_amount = 0
chotyry_syry_amount = 0


while True:
    print("1. Вибрати піццу")
    print("2. Вихід")
    print("3. Показати все замовлення")
    order = int(input("Що обираете?: "))

    if order == 1:
        print_menu()
        print('Введіть "stop", якщо бажаєте завершити')
        while True:
            pizza = input("Яку піццу бажаєте замовити?: ")

            if pizza == "stop":
                break

            if pizza == "Маргарита":
                count = int(input("Скільки штук бажаєте замовити?: "))
                if count > 0:
                    marharyta_amount += count
                    continue

            elif pizza == "Пепероні":
                count = int(input("Скільки штук бажаєте замовити?: "))
                if count > 0:
                    peperoni_amount += count
                    continue

            elif pizza == "Чотири сири":
                count = int(input("Скільки штук бажаєте замовити?: "))
                if count > 0:
                    chotyry_syry_amount += count
                    continue

            else:
                print("Назву піцци введено неправильно!")
                continue

    elif order == 2:
        print("Дякуємо що завітали!")
        break

    elif order == 3:
        print(
            "\n========== ВАШЕ ЗАМОВЛЕННЯ ========== "
            "\n\nПіца        Кількість      Вартість "
        )
        print("-" * 38)

        total_cost = 0

        if marharyta_amount > 0:
            cost = marharyta_amount * MARHARYTA
            total_cost += cost
            print(f"Маргарита          {marharyta_amount}      {cost} грн")

        if peperoni_amount > 0:
            cost = peperoni_amount * PEPERONI
            total_cost += cost
            print(f"Пепероні          {peperoni_amount}      {cost} грн")

        if chotyry_syry_amount > 0:
            cost = chotyry_syry_amount * CHOTYRY_SYRY
            total_cost += cost
            print(f"Чотири сири          {chotyry_syry_amount}      {cost} грн")

        print("\n" + "-" * 38)
        print(f"Загальна вартість:     {total_cost} грн ")
        print("=" * 38)
        print("\nДякуємо за замовлення!")
        break
