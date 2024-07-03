""" This script demonstrate the use of the datetime module for handling
    date anf times in python."""
from datetime import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print (f"Current date and time: {current_date.year}-{current_date.month}-{current_date.day} {current_date.hour}:{current_date.minute}:{current_date.second}")

def calculate_future_date(day):
    t_delta = datetime.timedelta(days=day)
    today = datetime.date.today()
    future_date = today + t_delta
    print (f"Future date: {future_date}")


display_current_datetime()
day = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(day)
