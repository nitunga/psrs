from datetime import datetime

year = int(input("Enter birth year : "))
month = int(input("Enter birth year :"))
day = int(input("Enter birth year : "))


def calculate_age(birth_year):
    today = datetime.today()
    age = today.year - birth_year.year - ((today.month, today.day) < (birth_year.month, birth_year.day))
    return age


birth_year = datetime(year, month, day)
age = calculate_age(birth_year)
print(age)
