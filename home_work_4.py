from datetime import * #імпортую всі методи з об'єкту datetime


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_greetings = [] #список в який зберігаю усі привітання які мають бути

    # цикл в якому аналізую усі дні народження та потім переношу їх у список вище
    for user in users:
        converted_birthdays = datetime.strptime(user['birthday'], '%Y.%m.%d').date() #форматую рядки в зрозумілий час для об'єкта datetime

        if converted_birthdays < today: #перевіряю чи при припадає день народження на цей рік,якщо ні,то розглядаю наступний рік
            converted_birthdays += timedelta(weeks=52)

        next_birthday = (converted_birthdays - today).days #розраховую дні до наступного дня народження

        # перевіряю на які дні неділі день народження перепадає
        if converted_birthdays.weekday() == 5:
            converted_birthdays += timedelta(days=2)

        elif converted_birthdays.weekday() == 6:
            converted_birthdays += timedelta(days=1)

        #додаю до списку привітань вже готовий результат,після виконання всіх умов вище
        if next_birthday <= 7:
           upcoming_greetings.append({"name": user["name"], "greetings_date": converted_birthdays.strftime("%Y-%m-%d")})


    return upcoming_greetings #повертаю готовий результат з обробленним список привітань


users = [
    {"name": "John Doe", "birthday": "1999.01.22"},
    {"name": "Jane Smith", "birthday": "2023.01.29"}
]


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
