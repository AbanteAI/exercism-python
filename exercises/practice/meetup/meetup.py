import datetime
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self):
        super().__init__("That day does not exist.")


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

    if week == "teenth":
        day = 13
        while True:
            meetup_date = datetime.date(year, month, day)
            if meetup_date.weekday() == days[day_of_week]:
                return meetup_date
            day += 1
            if day > 19:
                raise MeetupDayException()
    else:
        week_num = {"first": 0, "second": 1, "third": 2, "fourth": 3, "fifth": 4, "last": -1}
        first_day = datetime.date(year, month, 1)
        first_day_of_week = (days[day_of_week] - first_day.weekday()) % 7
        day = first_day_of_week + 1 + (7 * week_num[week])

        try:
            meetup_date = datetime.date(year, month, day)
        except ValueError:
            raise MeetupDayException()

        if week == "last":
            while meetup_date.weekday() != days[day_of_week] or meetup_date.month != month:
                day -= 1
                meetup_date = datetime.date(year, month, day)
        else:
            while meetup_date.weekday() != days[day_of_week]:
                day += 7
                try:
                    meetup_date = datetime.date(year, month, day)
                except ValueError:
                    raise MeetupDayException()

        return meetup_date
