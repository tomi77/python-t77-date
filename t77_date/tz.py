"""dateutil.tz related functions"""
from __future__ import print_function, division

from datetime import datetime

from dateutil.tz import tzlocal, tzutc


def _convert(value, tzfrom, tzto):
    """Convert datetime.datetime object between timezones"""
    if not isinstance(value, datetime):
        raise ValueError('value must be a datetime.datetime object')

    if value.tzinfo is None:
        value = value.replace(tzinfo=tzfrom)

    return value.astimezone(tzto)


def utc_to_local(value):
    """Convert datetime.datetime time from UTC to local time zone"""
    return _convert(value, tzutc(), tzlocal())


def local_to_utc(value):
    """Convert datetime.datetime time from local time zone to UTC"""
    return _convert(value, tzlocal(), tzutc())
