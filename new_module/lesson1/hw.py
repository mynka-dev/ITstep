# Task1 Користувач вводить рядок англійською мовою.
# Порахуйте скільки в ньому голосних літер(aeuio)
# Виправіть помилки в коді

text = input("Введіть рядок англійською мовою: ").strip().lower()

count = 0
for letter in text:
    if "a" or "e" or "u" or "i" or "o " in letter:
        count += 1

print(f"Кількість голосних літер: {count}")


# Task2
