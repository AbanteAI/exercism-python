# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self):
        pass


from datetime import date

def meetup(year, month, week, day_of_week):
    # Calculate the first day of the month
    first_day = date(year, month, 1)

    # Calculate the weekday of the first day
    first_weekday = first_day.weekday()

    # Calculate the target weekday
    target_weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(day_of_week)

    # Calculate the offset for the target weekday
    offset = (target_weekday - first_weekday) % 7

    # Calculate the date of the meetup based on the week descriptor
    if week == "teenth":
        # Find the first date in the range of "teenth" days
        for day in range(13, 20):
            meetup_date = date(year, month, day)
            if meetup_date.weekday() == target_weekday:
                return meetup_date
    elif week == "last":
        # Find the last date in the month with the target weekday
        last_day = date(year, month+1, 1) - timedelta(days=1)
        for day in range(last_day.day, last_day.day-7, -1):
            meetup_date = date(year, month, day)
            if meetup_date.weekday() == target_weekday:
                return meetup_date
    else:
        # Find the nth occurrence of the target weekday
        nth_occurrence = int(week[0])
        meetup_day = first_day + timedelta(days=offset + (nth_occurrence - 1) * 7)
        return meetup_day

class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self):
        pass
