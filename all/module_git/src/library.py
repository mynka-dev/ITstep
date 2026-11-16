print("Вітаємо вас у нашій бібліотеці")
print("Гарного вам дня!")
print()

while True:
    print("1. Отримати книжку")
    print("2. Вихід")
    choice = int(input("Що обираєте?: "))

    if choice == 1:
        name = input("Введіть ваше ім'я: ")
        book = input("Введіть назву книги: ")
        print(f"Книжка {book} видана читачеві {name}")
    elif choice == 2:
        break
