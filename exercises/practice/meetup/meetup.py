# subclassing the built-in ValueError to create MeetupDayException


from datetime import date
from calendar import monthrange

def meetup(year, month, week, day_of_week):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekdays = {day: i for i, day in enumerate(days_of_week)}

    teenth_days = [13, 14, 15, 16, 17, 18, 19]
    last_day = monthrange(year, month)[1]

    if week == "teenth":
        for day in teenth_days:
            meetup_date = date(year, month, day)
            if meetup_date.weekday() == weekdays[day_of_week]:
                return meetup_date

    if week == "last":
        for day in range(last_day, last_day - 7, -1):
            meetup_date = date(year, month, day)
            if meetup_date.weekday() == weekdays[day_of_week]:
                return meetup_date

    week_number = int(week[0])
    count = 0

    for day in range(1, last_day + 1):
        meetup_date = date(year, month, day)
        if meetup_date.weekday() == weekdays[day_of_week]:
            count += 1
            if count == week_number:
                return meetup_date
    pass
