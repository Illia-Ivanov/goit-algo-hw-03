from datetime import * # Importing all methods from the datetime module


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_greetings = []  # A list to store all upcoming greetings

    # A loop to analyze all birthdays and add them to the list above
    for user in users:
        converted_birthdays = datetime.strptime(user['birthday'], '%Y.%m.%d').date()  # Formatting strings into a date object

        if converted_birthdays < today: # Check if the birthday is in this year; if not, consider the next year
            converted_birthdays += timedelta(weeks=52)

        next_birthday = (converted_birthdays - today).days # Calculate days until the next birthday

         # Check what day of the week the birthday falls on
        if converted_birthdays.weekday() == 5:
            converted_birthdays += timedelta(days=2)

        elif converted_birthdays.weekday() == 6:
            converted_birthdays += timedelta(days=1)

        # Add the finalized result to the greetings list after satisfying all conditions above
        if next_birthday <= 7:
           upcoming_greetings.append({"name": user["name"], "greetings_date": converted_birthdays.strftime("%Y-%m-%d")})


    return upcoming_greetings # Return the processed list of greetings


users = [
    {"name": "John Doe", "birthday": "1999.01.22"},
    {"name": "Jane Smith", "birthday": "2023.01.29"}
]


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
