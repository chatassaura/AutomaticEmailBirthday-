import datetime as dt
import smtplib
import pandas as pd
import random
my_email = #SEU EMAIL / your email
my_password = #SUA SENHA / your password
# # 1. Update the birthdays.csv
# name = input("What's your friend name: ")
# email = input("What's your friend email: ")
# year = input("What's your friend year of birth: ")
# month = input("What's your friend month of birth: ")
# day = input("What's your friend day of birth: ")
# update = f"{name},{email},{year},{month},{day}\n"
#
# with open('birthdays.csv', 'a') as list_births:
#     list_births.writelines(update)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_tuple = (now.month, now.day)
births = pd.read_csv("birthdays.csv")
dict_births = {(data_row.month, data_row.day): data_row for (index, data_row) in births.iterrows()}
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
if today_tuple in dict_births:
    birthday_person = dict_births[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password )
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{content}")
        connection.close()

# 4. Send the letter generated in step 3 to that person's email address.
