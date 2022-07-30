from datetime import date
import calendar


DAYS_OF_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_YEARS = [year for year in range(1800, 2200) if calendar.isleap(year)]


def is_leap_year(year):
    if (year % 4) == 0:
        return True
    elif (year % 100) != 0:
        return False
    elif (year % 400) != 0:
        return False
    return True


def get_days_in_month(month, year):
    if is_leap_year(year) and month == 2:
        return 29
    else:
        return DAYS_OF_MONTHS[month-1]


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < get_days_in_month(month, year):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def testDaysBetweenDates():
    # test same day
    assert (daysBetweenDates(2017, 12, 30,
                             2017, 12, 30) == 0)
    # test adjacent days
    assert (daysBetweenDates(2017, 12, 30,
                             2017, 12, 31) == 1)
    # test new year
    assert (daysBetweenDates(2017, 12, 30,
                             2018, 1, 1) == 2)

    # test same day
    assert (daysBetweenDates(2020, 2, 15,
                             2020, 3, 5) == (date(2020, 3, 5) - date(2020, 2, 15)).days)

    assert (daysBetweenDates(2020, 2, 15,
                             2024, 3, 5) == (date(2024, 3, 5) - date(2020, 2, 15)).days)

    # test adjacent days
    assert (daysBetweenDates(2017, 12, 30,
                             2017, 12, 31) == 1)

    assert (daysBetweenDates(2017, 12, 31,
                             2018, 1, 1) == 1)

    # test adjacent days
    assert (daysBetweenDates(2017, 12, 31,
                             2018, 2, 1) == (date(2018, 2, 1) - date(2017, 12, 31)).days)

    assert (daysBetweenDates(2017, 12, 31,
                             2019, 2, 1) == (date(2019, 2, 1) - date(2017, 12, 31)).days)

    assert (daysBetweenDates(2016, 12, 31,
                             2019, 2, 1) == (date(2019, 2, 1) - date(2016, 12, 31)).days)
    # test new year
    assert (daysBetweenDates(2017, 12, 30,
                             2018, 1, 1) == 2)
    # test full year difference
    assert (daysBetweenDates(2012, 6, 29,
                             2013, 6, 29) == 365)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


if __name__ == "__main__":
    daysBetweenDates()

    print("end")
