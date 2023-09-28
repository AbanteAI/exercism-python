import datetime
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


def meetup(year, month, week, day_of_week):
    days = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }

        elif week == "last":
            start_date = datetime.date(year, month + 1, 1) - datetime.timedelta(days=7)
        else:
            start_date = datetime.date(year, month, 1)
        start_date = datetime.date(year, month, 1)
        weeks = {"first": 0, "second": 1, "third": 2, "fourth": 3, "fifth": 4}
        start_date += datetime.timedelta(weeks[week] * 7)

    day_diff = (days[day_of_week] - start_date.weekday()) % 7
    meetup_date = start_date + datetime.timedelta(day_diff)

    if meetup_date.month != month:
        raise MeetupDayException("That day does not exist.")

    return meetup_date
