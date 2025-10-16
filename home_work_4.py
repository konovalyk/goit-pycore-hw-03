from datetime import datetime, timedelta
import random
import re

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

def normalize_phone(phone_number):
    """
    This function normalizes a phone number by removing non-numeric characters
    and ensuring it has the correct length.
    :param phone_number: The phone number.
    """
    # Remove non-numeric characters
    cleaned = ''.join(filter(str.isdigit, phone_number))
    # Check if the cleaned number has the correct length
    if len(cleaned) == 10:
        return cleaned
    else:
        return "Invalid phone number format."



def normalize_phone(phone_number):
    """
    Normalize a phone number to international format +380XXXXXXXXX.
    Removes all characters except digits and '+' at the start.
    If the number starts with '380', adds only '+'.
    If the number is incomplete (less than 10 digits after country code),
    returns None.
    """
    # Remove all characters except digits and '+'
    cleaned = re.sub(r'[^\d+]', '', phone_number)
    # If number starts with '+', keep as is
    if cleaned.startswith('+'):
        cleaned = '+' + cleaned.lstrip('+')
        if not cleaned.startswith('+38'):
            cleaned = '+38' + cleaned.lstrip('+')
    # If number starts with '380', add '+'
    elif cleaned.startswith('380'):
        cleaned = '+' + cleaned
    # If number starts with 0 or other, add '+38'
    else:
        cleaned = '+38' + cleaned.lstrip('+')
    # Check if the normalized number has enough digits (should be +380XXXXXXXXX, 13 chars)
    if re.fullmatch(r'\+380\d{9}', cleaned):
        return cleaned
    else:
        return None

# Usage example:
raw_numbers = [
    "067123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "123",  
    "05012", 
]

# Only valid numbers will be included in the result
sanitized_numbers = [num for num in (normalize_phone(n) for n in raw_numbers) if num]
print("Sanitized phone numbers for SMS:", sanitized_numbers)

def get_upcoming_birthdays(users):
    """
    This function takes a list of dicts names and birthdates,
    and returns a  List of dicts names with celebrated dates within the next 7 days.
    If the birthday falls on a weekend, the date of the celebration is moved to the following Monday.
    :param users: List of dicts (name, birthdate) where birthdate is in 'YYYY-MM-DD' format.
    users = [
    {"name": "John Doe", "birthday": "1985-01-23"},
    {"name": "Jane Smith", "birthday": "1990-01-27"}
    ]
    :return: List of dicts names with celebrated dates where is in 'YYYY-MM-DD' format
    """
    today = datetime.today().date()
    upcoming = []

    for user in users:
        try:
            # Accept both 'YYYY-MM-DD' and 'YYYY.MM.DD' formats
            bday_str = user['birthday'].replace('.', '-')
            birth_date = datetime.strptime(bday_str, '%Y-%m-%d').date()
            this_year_birthday = birth_date.replace(year=today.year)

            # If birthday has already occurred this year, skip this user
            if this_year_birthday < today:
                continue
            # Calculate the difference in days
            delta_days = (this_year_birthday - today).days
            if 0 <= delta_days <= 7:
                celebration_date = this_year_birthday
                if celebration_date.weekday() in (5, 6):  # Saturday or Sunday
                    celebration_date += timedelta(days=(7 - celebration_date.weekday()))
                # Output date in 'YYYY.MM.DD' format
                upcoming.append({"name": user['name'], "celebration_date": celebration_date.strftime('%Y.%m.%d')})
        except ValueError:
            continue
    return upcoming
# Example usage:
users = [
    {"name": "John Doe", "birthday": "1985.10.18"},
    {"name": "Jane Smith", "birthday": "1990.10.27"},
    {"name": "Alice Johnson", "birthday": "1992.10.30"},
    {"name": "Bob Brown", "birthday": "1988.09.01"},
    {"name": "Charlie Davis", "birthday": "1995.11.03"},
]

print("Upcoming birthdays within the next 7 days:")
for celebration in get_upcoming_birthdays(users):
    print(f"{celebration['name']}: {celebration['celebration_date']}")