#Task1
size = input("Введіть розмір футболки(S, M, L, XL): ")
if size == "S" or size == "M":
    color = input("Введіть колір футболки: ")
    if color == "фіолетовий" or color == "жовтий":
        print(f"Немає у наявності футблока розмір {size} та колір {color}")
    else:
        print(f"Є у наявності футблока розмір {size} та колір {color}")
if size == "L":
    print(f"Всі футболки розміру {size} закінчились")
if size == "XL":
    fabric = input("Який тип тканини?: ")
    if fabric != "бавовна":
        print(f"Немає в наявності футблоки у розмірі {size} з тканини {fabric}"
                f"\nЄ лише бавовна")
    else:
        print(f"Є в наявності футблоки у розмірі {size} з тканини {fabric}")



