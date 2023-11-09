# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message="Invalid meetup day or count"):
        super().__init__(message)


import calendar

def meetup(year, month, week, day_of_week):
    # Define a dictionary to map weekday names to weekday numbers
    weekdays = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    # Check if the day_of_week is valid
    if day_of_week not in weekdays:
        raise MeetupDayException(f"Invalid weekday name: {day_of_week}")

    # Define a dictionary to map week descriptor to a function that finds the correct day
        "first": lambda days: days[0],
        "second": lambda days: days[1],
        "third": lambda days: days[2],
        "fourth": lambda days: days[3],
        "fifth": lambda days: days[4] if len(days) > 4 else None,
        "last": lambda days: days[-1],
        "teenth": lambda days: next(day for day in days if 13 <= day <= 19)
    }

    # Check if the week descriptor is valid
    if week not in week_descriptors:
        raise MeetupDayException(f"Invalid week descriptor: {week}")

    # Find all days of the specified day_of_week in the given month and year
    month_days = calendar.monthcalendar(year, month)
    days_of_week = [day[weekdays[day_of_week]] for day in month_days if day[weekdays[day_of_week]] != 0]

    # Find the correct day using the week descriptor
    try:
        meetup_day = week_descriptors[week](days_of_week)
        if meetup_day is None:
            raise MeetupDayException(f"The {week} {day_of_week} does not exist in {calendar.month_name[month]} {year}")
    except IndexError:
        raise MeetupDayException(f"The {week} {day_of_week} does not exist in {calendar.month_name[month]} {year}")

    return datetime.date(year, month, meetup_day)
