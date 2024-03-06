import os
from dotenv import load_dotenv
import smtplib
import random
import datetime as dt

# Loading environment variables including your email and app password from the .env file
load_dotenv(dotenv_path="./secrets.env")
EMAIL = os.getenv('EMAIL')
PWD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')

letter_choice = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

# Using the datetime module to identify today's date
now = dt.datetime.now()
month = now.month
day = now.day

birthday_people = {}

# Opening the birthdays.csv file and comparing the birthdays to today's date to determine whose birthday is today
with open("birthdays.csv") as file:
    lines = file.readlines()
    lines.remove(lines[0])
    for i in lines:
        lines_split = i.split(',')
        birth_month = int(lines_split[3])
        birth_day = int(lines_split[4].strip())
        print(birth_month)
        if month == birth_month and day == birth_day:
            # Updating the birthday_people dictionary with names and emails of people whose birthday it is today.
            birthday_people.update({lines_split[0]: lines_split[1]})

# Iterating over the birthday_people dictionary to automatically send a birthday greeting email
for key in birthday_people:
    person = key
    person_email = birthday_people[key]
    letter = random.choice(letter_choice)
    with open(letter) as file:
        message = file.read()
        message = message.replace("[NAME]", person)
    with smtplib.SMTP(HOST, 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PWD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=person_email,
            msg=f"Subject: Happy Birthday!\n\n{message}"
        )
