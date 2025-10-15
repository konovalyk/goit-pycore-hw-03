from datetime import datetime 
import random


def get_days_from_today(date):

    """
    This function takes a date string in the format 'YYYY-MM-DD' \
        and returns the number of days from today to that date.
    If the date is in the future, it returns a negative number.
    """
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - target_date
        return delta.days
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'."
# Example usage:
delta_days = get_days_from_today('2025-12-25')
print(f"Days from today to the target date: {delta_days}")


def get_numbers_ticket(min, max, quantity):
    """
    This function generates a list of unique random numbers within a specified range.
    :param min: Minimum number in the range >= 1(inclusive).
    :param max: Maximum number in the range <= 1000 (inclusive).
    :param quantity: Number of unique random numbers to generate.
    :return: List of unique random numbers.
    """
    
    result = sorted(random.sample(range(min, max + 1), quantity))
    return result

# Example usage:

while True:
    user_input = input("Input min, max, quantity separated by commas: ")
    min_val, max_val, quantity = map(int, user_input.split(","))
    if quantity > (max_val - min_val + 1) or min_val > max_val\
          or min_val < 1 or max_val > 1000 or quantity < 1:
        print("Invalid input. Please ensure min <= max and quantity is within\
               the range and min >= 1 and max <= 1000.")
        continue
    else:
        print(get_numbers_ticket(min_val, max_val, quantity))
        break


