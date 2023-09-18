import datetime
import calendar
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self):
        pass


def meetup(year, month, week, day_of_week):
    day_mapping = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    week_mapping = {
        "first": 1,
        "second": 2,
        "third": 3,
        "fourth": 4,
        "fifth": 5,
        "last": -1,
        "teenth": 0
    }
    }

    day_num = day_mapping[day_of_week]
    week_num = week_mapping[week]

    if week_num == 0:
        start_date = datetime.date(year, month, 13)
        end_date = datetime.date(year, month, 19)
    else:
        start_date = datetime.date(year, month, 1)
        end_date = datetime.date(year, month, calendar.monthrange(year, month)[1])

    for day in range(start_date.day, end_date.day + 1):
        current_date = datetime.date(year, month, day)
        if current_date.weekday() == day_num:
            if week_num > 0:
            if week_num > 0:
                week_num -= 1
            elif week_num == -1 and current_date.day + 7 > end_date.day:
                return current_date
            elif week_num == 0 and 13 <= current_date.day <= 19:
                return current_date
            elif week_num == 5 and current_date.day + 7 > end_date.day:
                return current_date

    raise MeetupDayException()
