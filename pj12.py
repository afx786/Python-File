def is_leap_year(year):
    """Check if the given year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_num_days_in_month(year, month):
    """Get the number of days in the given month of the given year."""
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28

def display_calendar(year, month):
    """Display the calendar for the specified month and year."""
    # Get the number of days in the month
    num_days = get_num_days_in_month(year, month)

    # Print the header
    print(f"{' ' * 15}{month}/{year}")
    print("Su Mo Tu We Th Fr Sa")

    # Get the day of the week for the first day of the month (0 for Sunday, 6 for Saturday)
    first_day_of_week = (1 + sum(get_num_days_in_month(year, m) for m in range(1, month))) % 7

    # Print the days of the month
    day = 1
    for _ in range(6):
        week = ""
        for i in range(7):
            if _ == 0 and i < first_day_of_week:
                week += "   "
            elif day <= num_days:
                week += f"{day:2d} "
                day += 1
            else:
                week += "   "
        print(week)

# Input year and month from the user
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Display the calendar
display_calendar(year, month)
