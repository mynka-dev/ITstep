print("Вітаємо вас у нашій бібліотеці")
print("Гарного вам дня!")
print()

while True:
    print("1. Отримати книжку")
    print("2. Повернути книжку")
    print("3. Вихід")
    choice = int(input("Що обираєте?: "))

    if choice == 1:
        name = input("Введіть ваше ім'я: ")
        book = input("Введіть назву книги: ")
        print(f"Книжка {book} видана читачеві {name}")
    elif choice == 2:
        name = input("Введіть ваше ім'я: ")
        book = input("Введіть назву книги: ")
        print(f"Читач {name} повернув книгу {book}")
    elif choice == 3:
        break
