from datetime import *


def get_days_from_today(date_string):
    #Тут виконується обробка днів від сьогодні до певної вказанної дати,яку ввів користувач
    now = datetime.today().date() #встановлюємо об'єкту datetime сьогоднішню дату без часу
    input_date = datetime.strptime(date_string, '%Y-%m-%d').date() #приводимо рядок користувача у формат дати
    delta = now - input_date #Виконуємо розрахунок,від поточної дати віднімаємо введену дату користувачем
    return delta.days #повертаємо розрахунок в днях

#Введення даних користувачем та виввід результату функції
enter_days = input('Введіть дату яку потрібно порахувати від сьогодні у форматі РРРР-ММ-ДД: ')
result = get_days_from_today(enter_days)
print(f'Кількість днів яка пройшла з часу який ви вказали: {result}')
