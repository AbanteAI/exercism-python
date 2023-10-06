# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self):
        pass


def meetup(year, month, week, day_of_week):
    import calendar
    import datetime

    # Get the weekday of the first day of the month
    first_day_weekday = calendar.weekday(year, month, 1)

    # Get the weekday of the desired day_of_week
    desired_weekday = list(calendar.day_name).index(day_of_week)

    # Calculate the offset to the desired day_of_week
    offset = (desired_weekday - first_day_weekday) % 7

    # Calculate the day of the meetup
    if week == "teenth":
        day = offset + 13
    elif week == "last":
        last_day = calendar.monthrange(year, month)[1]
        day = last_day - (7 - offset) + 1
    elif week.isdigit() and int(week) > 0:
        day = offset + (int(week) - 1) * 7 + 1
    else:
        raise MeetupDayException("Invalid week input")

    return datetime.date(year, month, day)
