from datetime import timedelta


def start_of_day(date):
    """

    :param date: Date to ...
    :type date: datetime.datetime
    :rtype: datetime.datetime
    """
    return date.replace(hour=0, minute=0, second=0, microsecond=0)


def end_of_day(date):
    """

    :param date: Date to ...
    :type date: datetime.datetime
    :rtype: datetime.datetime
    """
    return start_of_day(date) + timedelta(days=1, microseconds=-1)


def start_of_month(date):
    """

    :param date: Date to ...
    :type date: datetime.datetime
    :rtype: datetime.datetime
    """
    return start_of_day(date).replace(day=1)


def end_of_month(date):
    """

    :param date: Date to ...
    :type date: datetime.datetime
    :rtype: datetime.datetime
    """
    if date.month == 12:
        return start_of_month(date).replace(year=date.year + 1, month=1) - timedelta(microseconds=1)
    else:
        return start_of_month(date).replace(month=date.month + 1) - timedelta(microseconds=1)
