import datetime
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message="That day does not exist."):
        super().__init__(message)


def meetup(year, month, week, day_of_week):
    pass

def first_day_of_month(year, month):
    return datetime.date(year, month, 1)

def last_day_of_month(year, month):
    if month == 12:
        return datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        return datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)

def meetup(year, month, week, day_of_week):
    days = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    first_day = first_day_of_month(year, month)
    last_day = last_day_of_month(year, month)
    current_day = first_day + datetime.timedelta(days=(days[day_of_week] - first_day.weekday()) % 7)

    if week == "teenth":
        while current_day.day < 13:
            current_day += datetime.timedelta(days=7)
        return current_day
    elif week in ["first", "second", "third", "fourth"]:
        week_number = {"first": 1, "second": 2, "third": 3, "fourth": 4}
        current_day += datetime.timedelta(days=7 * (week_number[week] - 1))
        if current_day > last_day:
            raise MeetupDayException("That day does not exist.")
        return current_day
    elif week == "last":
        while current_day + datetime.timedelta(days=7) <= last_day:
            current_day += datetime.timedelta(days=7)
        return current_day
    else:
        raise MeetupDayException("Invalid week descriptor.")