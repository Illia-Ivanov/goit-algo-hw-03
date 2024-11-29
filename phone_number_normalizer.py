import re


def normalize_phone(phone_number):
    # here phone numbers are corrected
    converted_number = r'[^\+\d]' # select which characters remain in the string, namely + and all digits
    replacement = r'' # specify that all other characters are replaced with nothing
    result = re.sub(converted_number, replacement, phone_number) # using this method, process the string and remove unnecessary characters
    # check for + and whether the country code is specified
    if not result.startswith('+') and not result.startswith('38'):
        result = '38' + result
    if not result.startswith('+'):
        result = '+' + result

    return result


# A list reformatted using list comprehension and our function into a list of properly converted numbers
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
