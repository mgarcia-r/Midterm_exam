def leap_year(year):
    """
    Checks if a year is a lep year
    :param year: the year
    :return: true if the year is leap, false if it is not
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_since_birth(birthday):
    """
    Calculates the number of days that have passed since birth,counting only the full years in between (excluding the birth year and current year).
    :param birthday: A string in the format "DD-MM-YYYY"
    :return: The number of days in the full years between birth and today
    """
    # Extract the birth year from the input string
    birth_year = int(birthday.split("-")[2])
    current_year = 2025

    if birth_year == current_year:
        return 0  # No full years have passed

    start_year = birth_year + 1  # First full year after birth
    end_year = current_year - 1  # Last full year before today

    # Count the total days in all full years
    total_days = 0
    for year in range(start_year, end_year + 1):
        total_days += 366 if leap_year(year)  else 365

    return total_days

print(days_since_birth("07-02-2005"))

