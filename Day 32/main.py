import smtplib
import datetime as dt
import random

MY_EMAIL = "abc@email.com"
PASSWORD = "1234abcd"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="xyz@yahoo.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}")

# import smtplib
#
# my_email = "user@email.com"  # User email
# password = "abc123"  # User password
#
# # Need to lower mail security level to make this work
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="xyz@yahoo.com",  # Receiver email
#                         msg="Subject:Hello\n\nThis is the body of my email.")

# import datetime as dt
#
# now = dt.datetime.now()
# print(now)