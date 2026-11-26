# Task1


# text = input("Введіть текст: ")
#
# while True:
#     index = int(input("Введіть індекс: "))
#     if index <= len(text):
#         print(text[index])
#         break
#     else:
#         print(f"Індекс завеликий(максимальний індекс -- {len(text) - 1})")


# Task2

# text = input("Введіть рядок: ")
#
# start = int(input("Введіть початковий індекс: "))
# end = int(input("Введіть кінцевий індекс: "))
#
# segment = text[start:end]
#
# print(segment)


# Task3


# text = input("Введіть текст: ")
# index = int(input("Введіть число: "))
#
# print(f" до індекса {index} -- {text[:index]}")
# print(f" після індекса {index} -- {text[index:]}")


# Task4

# text = input("Введіть текст: ")
#
# if text[-1] in ".!?":
#     print("Знак є ")
# else:
#     print("Знак відсутній")


# Task5


# text = input("Введіть рядок: ")
#
# if text[0].isupper():
#        print("Перший символ — велика літера")
#
# else:
#     print("Перший символ — не велика літера")


# АбО


# text = input("Введіть рядок: ")
#
# if text[0].isupper():
#     print("Перший символ — велика літера")
# else:
#     print("Перший символ — не велика літера")


# Task6
#
# text = input("Введіть рядок: ").lower().replace(" ", "")
#
# if text[::-1] == text:
#     print("Це паліндром")
# else:
#     print("Це не паліндром")


# Task7
gerund = ""
past_tense = ""
vowel_start = ""
other = ""

while True:
    word = input("Введіть слово: ").strip()
    word_lower = word.lower()
    if word == "END":
        break
    if word_lower.endswith("ing"):
        gerund += word + " "
    elif word_lower.endswith("ed"):
        past_tense += word + " "
    elif word_lower and word[-1] in "aeuio":
        vowel_start += word + " "
    else:
        other += word + " "
print(
    f"\ngerund --- {gerund}"
    f"\npast_tense --- {past_tense}"
    f"\nvowel_start --- {vowel_start}"
    f"\nothers --- {other}"
)
