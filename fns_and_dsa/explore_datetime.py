import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current date and time: ", current_date)
display_current_datetime()


def calculate_future_date():
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=7)
    print("Future date:", future_date)

fututredate = input("Enter the number of days to add to the current date: ")
calculate_future_date() 