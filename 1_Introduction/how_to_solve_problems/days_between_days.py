from datetime import date

DAYS_OF_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def _extract_months_days_between_dates(month1, month2):
    """
    :param month1: starting  month
    :param month2: ending month
    :return: 
        examples:
        month1=1, month2=3 -> output= [28] # February days
        month1=1, month2=5 -> output= [28, 31, 30] # February, March and April days
        month1=11, month2=2 -> output= [31, 31] # December and January days
        month1=11, month2=12 -> output= [0] # 0 days
        month1=12, month2=1 -> output= [0] # 0 days
    """
    if abs(month1 - month2) < 2:
        return [0]
    elif month2 > month1:
        extracted_days = DAYS_OF_MONTHS[month1:month2 - 1]
        return extracted_days
    else:
        till_end_of_year = DAYS_OF_MONTHS[month1:12] if month1 < 12 else []
        from_the_start_of_the_year = DAYS_OF_MONTHS[0:(month2 - 1)] if month1 > 1 else []
        extracted_days = till_end_of_year + from_the_start_of_the_year
        return extracted_days


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    It ignores leap years
    """
    if (year1, month1, day1) == (year2, month2, day2):
        return 0

    if (month1, day1) == (month2, day2):
        delta_years = abs(year2 - year1)
        return delta_years * sum(DAYS_OF_MONTHS)

    nb_days = DAYS_OF_MONTHS[month1 - 1] - day1
    nb_days += day2

    if month1 != month2 and abs(month1 - month2) > 1:
        extracted_days = _extract_months_days_between_dates(month1, month2)
        nb_days += sum(extracted_days)
    elif month1 == month2 and year1 == year2:
        return day2 - day1

    delta_years = abs(year2 - year1) - 1
    nb_days += delta_years * sum(DAYS_OF_MONTHS)
    return nb_days


def testDaysBetweenDates():
    # test same day
    assert (daysBetweenDates(2017, 12, 30,
                             2017, 12, 30) == 0)
    # test adjacent days
    assert (daysBetweenDates(2017, 12, 30,
                             2017, 12, 31) == 1)

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
    testDaysBetweenDates()

    print("end")
