import calendar
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self):
        pass


def meetup(year, month, week, day_of_week):
    day_map = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    day_num = day_map[day_of_week]
    month_calendar = calendar.Calendar().monthdayscalendar(year, month)

    if week == "teenth":
        for week in month_calendar:
            if 13 <= week[day_num] <= 19:
                return date(year, month, week[day_num])
    elif week == "last":
        for week in reversed(month_calendar):
            if week[day_num] != 0:
                return date(year, month, week[day_num])
    else:
        count = int(week[0])
        valid_days = [week[day_num] for week in month_calendar if week[day_num] != 0]
        if count <= len(valid_days):
            return date(year, month, valid_days[count - 1])
        else:
            raise MeetupDayException("That day does not exist.")
