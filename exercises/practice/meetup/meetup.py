import calendar
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message="That day does not exist."):
        super().__init__(message)


def meetup(year, month, week, day_of_week):
    day_name_to_num = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    day_num = day_name_to_num[day_of_week]

    if week == "teenth":
        for day in range(13, 20):
            if calendar.weekday(year, month, day) == day_num:
                return date(year, month, day)
    else:
        count = 0
        if week == "last":
            days_in_month = calendar.monthrange(year, month)[1]
            day_range = range(days_in_month, 0, -1)
        else:
            week_num = int(week[0])
            day_range = range(1, calendar.monthrange(year, month)[1] + 1)

        for day in day_range:
            if calendar.weekday(year, month, day) == day_num:
                count += 1
                if count == week_num:
                    return date(year, month, day)

    raise MeetupDayException()
