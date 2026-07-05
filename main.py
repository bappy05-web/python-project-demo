from datetime import date


def calculate_age(birth_date):
    today = date.today()

    # Check if the birthday has passed this year
    # A boolean evaluates to 1 (True) or 0 (False)
    has_birthday_passed = (today.month, today.day) < (birth_date.month, birth_date.day)

    # Subtracting the boolean handles the birthday buffer automatically
    age = today.year - birth_date.year - has_birthday_passed
    return age


def main():
    print("--- Python Age Calculator ---")
    try:
        # Requesting inputs separately to avoid formatting errors
        year = int(input("Enter birth year (YYYY): "))
        month = int(input("Enter birth month (1-12): "))
        day = int(input("Enter birth day (1-31): "))

        user_birthday = date(year, month, day)
        age = calculate_age(user_birthday)

        print(f"\nYou are {age} years old.")

    except ValueError:
        print("\nInvalid entry. Please enter correct numeric calendar dates.")


if __name__ == '__main__':
    main()

