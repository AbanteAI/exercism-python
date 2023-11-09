# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message="Meetup day is invalid"):
        super().__init__(message)


import calendar

def meetup(year, month, week, day_of_week):
    # Mapping weekday names to weekday numbers
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
        raise MeetupDayException(f"Invalid day of the week: {day_of_week}")

    # Find the first day of the month and the number of days in the month
    first_day_of_month, number_of_days_in_month = calendar.monthrange(year, month)
    day = weekdays[day_of_week] - first_day_of_month

    if day < 0:
        day += 7

    if week == 'teenth':
        day += (13 - day) % 7
    elif week == 'last':
        while day + 7 <= number_of_days_in_month:
            day += 7
        elif week == 'fifth':
            day += 28
            if day > number_of_days_in_month:
                raise MeetupDayException("The fifth meetup day does not exist in this month")
    else:
        weeks = {
            'first': 0,
            'second': 1,
            'third': 2,
            'fourth': 3
        }
        if week not in weeks:
            raise MeetupDayException(f"Invalid week descriptor: {week}")
        day += weeks[week] * 7

    meetup_day = day + 1
    if meetup_day > number_of_days_in_month:
        raise MeetupDayException("The meetup day does not exist in this month")

    return datetime.date(year, month, meetup_day)
