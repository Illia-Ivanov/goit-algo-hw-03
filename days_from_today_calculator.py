from datetime import *


def get_days_from_today(date_string):
    # Here the number of days from today to a specific date entered by the user is calculated
    now = datetime.today().date() # Set today's date without the time for the datetime object
    input_date = datetime.strptime(date_string, '%Y-%m-%d').date()  # Convert the user's string into a date format
    delta = now - input_date # Perform the calculation by subtracting the entered date from the current date
    return delta.days # Return the calculation in days

# User input and output of the function result
enter_days = input('Введіть дату яку потрібно порахувати від сьогодні у форматі РРРР-ММ-ДД: ')
result = get_days_from_today(enter_days)
print(f'Кількість днів яка пройшла з часу який ви вказали: {result}')
