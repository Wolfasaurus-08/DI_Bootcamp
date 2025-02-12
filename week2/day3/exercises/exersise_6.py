# Exercise 6 : Birthday and minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), 
# then displays a message stating how many minutes the user lived in his life.
import datetime

def minutes_lived(birthdate):
    birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
    now = datetime.datetime.now()
    minutes = (now - birthdate).total_seconds() / 60
    print(f"You have lived for approximately {int(minutes)} minutes.")

minutes_lived("2000-01-01")