from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    # Display current date and time
    current_date = display_current_datetime()
    
    # Prompt user for number of days
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        if days_to_add < 0:
            print("Please enter a non-negative number of days.")
            return
        # Calculate and display future date
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()