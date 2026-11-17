print("Вітаємо вас у нашій бібліотеці")
print("Гарного вам дня!")
print()

while True:
    choice = int(
        input("1. Отримати книжку \n2. Повернути книжку \n3. Вихід \nЩо обираєте?: ")
    )

    if choice == 1 or choice == 2:
        name = input("Введіть ваше ім'я: ")
        book = input("Введіть назву книги: ")

        if not name or not book:
            print("Ім'я та назва книжки не можуть бути порожніми!")
            continue

        if choice == 1:
            period = int(input("На скільки днів берети книгу?: "))
            if period < 0:
                print("Кількість днів не може бути від'ємною!")
                continue
            if period > 30:
                print("Книжку видають максимум на 30 днів!")
                continue
            print(f"Книжка {book} видана читачеві {name} на {period} днів")
            choice = input("Щось ще?: ")
            if choice == "так":
                continue
            else:
                break
        elif choice == 2:
            print(f"Читач {name} повернув книгу {book}")
            choice = input("Щось ще?: ")
            if choice == "так":
                continue
            else:
                break

    elif choice == 3:
        break
