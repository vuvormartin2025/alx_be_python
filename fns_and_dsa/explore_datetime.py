from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(current_date):
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=number_of_days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer for the number of days.")

# Run the script
if __name__ == "_main_":
    current = display_current_datetime()
    calculate_future_date(current)