print("\033[1mВітаємо вас у нашій піцерії\033[0m")

MARHARYTA = 150
PEPERONI = 180
CHOTYRY_SYRY = 200


marharyta_amount = 0
peperoni_amount = 0
chotyry_syry_amount = 0


def print_menu():
    width = 30
    print("╔" + "═" * width + "╗")
    print(f"║{'МЕНЮ':^{width}}║")
    print("╠" + "═" * width + "╣")
    print(f"║ {'1. Маргарита     -  150грн':<{width - 1}}║")
    print(f"║ {'2. Пепероні      -  180грн':<{width - 1}}║")
    print(f"║ {'3. Чотири сири   -  200грн':<{width - 1}}║")
    print("╚" + "═" * width + "╝")


while True:
    print("\n1. Вибрати піцу")
    print("2. Вихід")
    order = int(input("Що обираєте?: "))

    if order == 1:
        print_menu()
        pizza = input("Яку саме бажаєте?: ")

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
        break
    else:
        print("Неправильний вибір пункту. Спробуйте ще раз.")
