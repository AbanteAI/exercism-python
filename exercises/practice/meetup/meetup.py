import datetime
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message="Invalid meetup day or week combination"):
        super().__init__(message)
        self.message = message


import calendar

def meetup(year, month, week, day_of_week):
    # Constants for the descriptor
    weekdays = {
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
        'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6
    }
    teenth_days = [13, 14, 15, 16, 17, 18, 19]
    week_number = {
        '1st': 1, 'first': 1,
        '2nd': 2, 'second': 2,
        '3rd': 3, 'third': 3,
        '4th': 4, 'fourth': 4,
        '5th': 5, 'fifth': 5,
        'last': -1
    }

    # Get the weekday number
    if day_of_week not in weekdays:
        raise MeetupDayException(f"Invalid day of the week: {day_of_week}")

    day_num = weekdays[day_of_week]

    # Calculate the date
    if week in week_number:
        return nth_weekday(year, month, day_num, week_number[week])
    elif week == 'teenth':
        return teenth_weekday(year, month, day_num)
    else:
        raise MeetupDayException(f"Invalid week descriptor: {week}")

def nth_weekday(year, month, weekday, n):
    # Find the first occurrence of the given weekday in the month
    month_calendar = calendar.monthcalendar(year, month)
    first_weekday = next((week[weekday] for week in month_calendar if week[weekday] != 0), None)

    if first_weekday is None:
        raise MeetupDayException("The weekday does not occur in the given month.")

    if n > 0:
        # Calculate the nth weekday of the month
        day = first_weekday + (n - 1) * 7
        if not valid_date(year, month, day):
            raise MeetupDayException(f"The {n}th {calendar.day_name[weekday]} does not exist in {calendar.month_name[month]} {year}.")
        return datetime.date(year, month, day)
    else:
        # Calculate the last weekday of the month
        last_weekday = next((week[weekday] for week in reversed(month_calendar) if week[weekday] != 0), None)
        if last_weekday is None:
            raise MeetupDayException("The weekday does not occur in the given month.")
        return datetime.date(year, month, last_weekday)

def teenth_weekday(year, month, weekday):
    month_calendar = calendar.monthcalendar(year, month)
    for day in teenth_days:
        week = (day - 1) // 7
        if month_calendar[week][weekday] == day:
            return datetime.date(year, month, day)
    raise MeetupDayException("Cannot find a teenth weekday in the given month.")

def valid_date(year, month, day):
    try:
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False
