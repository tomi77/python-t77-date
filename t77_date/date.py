# -*- coding: utf-8 -*-
from datetime import timedelta

from dateutil.relativedelta import relativedelta


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
    return start_of_month(date) + relativedelta(months=1) - timedelta(microseconds=1)
