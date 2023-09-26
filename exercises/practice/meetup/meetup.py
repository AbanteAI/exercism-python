# subclassing the built-in ValueError to create MeetupDayException
from datetime import date, timedelta
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self):
        pass


from datetime import date

def meetup(year, month, week, day_of_week):
    weekdays = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }
    
    teenth_days = [13, 14, 15, 16, 17, 18, 19]
    
    first_day_of_month = date(year, month, 1)
    first_weekday = first_day_of_month.weekday()
    
    if week == 'teenth':
        for day in teenth_days:
            meetup_date = date(year, month, day)
            if meetup_date.weekday() == weekdays[day_of_week]:
                return meetup_date
    elif week == 'last':
        last_day_of_month = date(year, month + 1, 1) - timedelta(days=1)
        last_weekday = last_day_of_month.weekday()
        for day in range(last_day_of_month.day - 6, last_day_of_month.day + 1):
            meetup_date = date(year, month, day)
            if meetup_date.weekday() == weekdays[day_of_week]:
                return meetup_date
    else:
        day = (week - 1) * 7 + (weekdays[day_of_week] - first_weekday + 7) % 7 + 1
        meetup_date = date(year, month, day)
        return meetup_date
