print("Вітаємо вас у нашій піцерії")
print("1. Вибрати піццу")
print("2. Вихід")
amount = 0
while True:
    order = int(input("Що обираете?: "))
    if order == 1:
        pizza = input("Яку саме бажаєте?: ")
        amount += 1
    elif order == 2:
        break
    print(f"Замовлено {pizza}, {amount} шт")
