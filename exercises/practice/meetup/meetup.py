import datetime
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        super().__init__(message)


import calendar

def meetup(year, month, week, day_of_week):
    # Define the mapping of weekdays to their respective index (Monday=0, ..., Sunday=6)
    weekdays = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    # Check if the day_of_week is valid
    if day_of_week not in weekdays:
        raise MeetupDayException(f"Invalid day of the week: {day_of_week}")

    # Create a calendar for the given month and year
    month_calendar = calendar.monthcalendar(year, month)
    day_index = weekdays[day_of_week]

    # Function to find the meetup day
    def find_meetup_day(week_descriptor):
        if week_descriptor == "teenth":
            for week in month_calendar:
                if 13 <= week[day_index] <= 19:
                    return week[day_index]
        elif week_descriptor == "last":
            for week in reversed(month_calendar):
                if week[day_index] != 0:
                    return week[day_index]
        else:
            week_counts = {
                "first": 0,
                "second": 1,
                "third": 2,
                "fourth": 3,
                "fifth": 4
            }
            if week_descriptor in week_counts:
                week_number = week_counts[week_descriptor]
                try:
                    if month_calendar[week_number][day_index] != 0:
                        return month_calendar[week_number][day_index]
                except IndexError:
                    pass
            else:
                raise MeetupDayException(f"Invalid week descriptor: {week_descriptor}")

        raise MeetupDayException(f"No such day exists: {week_descriptor} {day_of_week}")

    # Find the day of the meetup
    meetup_day = find_meetup_day(week)
    return datetime.date(year, month, meetup_day)

# Import datetime at the beginning of the file
