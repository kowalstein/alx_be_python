""" This script demonstrate the use of the datetime module for handling
    date and times in python."""
from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print (formatted)

def calculate_future_date(day):
    t_delta = timedelta(days=day)
    today = date.today()
    future_date = today + t_delta
    print (f"Future date: {future_date}")

display_current_datetime()
day = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(day)
