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

    # Create a calendar object for the month
    cal = calendar.Calendar()

    # Generate a list of all dates in the month that match the given day_of_week
    matching_days = [day for day in cal.itermonthdays2(year, month) if day[0] != 0 and day[1] == weekdays[day_of_week]]

    # Define a dictionary to map week descriptors to functions that return the correct date
    week_descriptors = {
        "fifth": lambda days: days[4][0] if len(days) > 4 else None,
        "last": lambda days: days[-1][0],
        "teenth": lambda days: next(day[0] for day in days if 13 <= day[0] <= 19)
    }

    # Check if the week descriptor is valid
    if week not in week_descriptors:
        raise MeetupDayException(f"Invalid week descriptor: {week}")

    # Find the day of the meetup
    # Find the day of the meetup
    meetup_day = week_descriptors[week](matching_days)
    if meetup_day is None:
        raise MeetupDayException(f"The fifth {day_of_week} does not exist in {calendar.month_name[month]} {year}")

    # Return the date of the meetup
    return datetime.date(year, month, meetup_day)
