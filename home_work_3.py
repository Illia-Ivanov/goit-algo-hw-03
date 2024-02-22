import re


def normalize_phone(phone_number):
    #тут виконується коррекція номерів
    converted_number = r'[^\+\d]' #вибираємо які символи остаються в рядку,а тобто + та усі цифри
    replacement = r'' #далі вказуємо що всі інші рядки змінюємо на пустоту
    result = re.sub(converted_number, replacement, phone_number) #завдяки цьому методу виконуємо вставку обробленного рядку та зміну непотрібних нам символів
    #виконуємо перевірку на + та чи вказанний код країни
    if not result.startswith('+') and not result.startswith('38'):
        result = '38' + result
    if not result.startswith('+'):
        result = '+' + result

    return result


#Список який переформатовуємо завдяки генерації списку та нашої функції в список з правильно конвертованими номерами
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11    ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)