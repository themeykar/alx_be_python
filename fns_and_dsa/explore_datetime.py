from datetime import datetime, date, timedelta


def display_current_datetime():
    current_date = datetime.now().replace(microsecond=0)
    print(f"Current date and time: {current_date}")

display_current_datetime()

def calculate_future_date():
    today = date.today()
    days_number = int(input("Enter number of days: "))
    future_date = today + timedelta(days_number)
    print(f"Future date: {future_date}")

calculate_future_date()