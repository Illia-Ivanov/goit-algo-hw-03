import random


def get_numbers_ticket(min, max, quantity):
    # Тут Виконуеться перевірка введенних даних на виключенння які можуть статися при введенні
    if min < 1 and max > 1000:
        return print('Число має бути більше ніж 1 та меньше ніж 1000!')
    elif min < 1:
        return print('Число має бути не меньше аніж 1!')
    elif max > 1000:
        return print('Число не має бути більше аніж 1000!')
    else:
        # Тут виконується генерація чисел в заданному діапазоні та кількість цих унікальних чисел
        rand_nums = []
        for i in range(quantity):
            generated_numbers = random.randint(min, max)
            rand_nums.append(generated_numbers)
        result = sorted(set(rand_nums))
        return result

#Введення даних користувачем та виввід результату функції
minimal_number = int(input('Ввведіть число,яке не меньше за 1: '))
maximal_number = int(input('Введіть число,яке не більше за 1000: '))
quantity_sum = int(input('Введіть потрібну кількість чисел, які потрібно обрати: '))
result = get_numbers_ticket(minimal_number, maximal_number, quantity_sum)
print(result)
