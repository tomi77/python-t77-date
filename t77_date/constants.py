"""Date related constants"""
import re


HOURS_IN_DAY = 24

MINUTES_IN_HOUR = 60
MINUTES_IN_DAY = MINUTES_IN_HOUR * HOURS_IN_DAY

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = SECONDS_IN_MINUTE * MINUTES_IN_HOUR
SECONDS_IN_DAY = SECONDS_IN_HOUR * HOURS_IN_DAY

MICROSECONDS_IN_SECOND = 1000000
MICROSECONDS_IN_MINUTE = MICROSECONDS_IN_SECOND * SECONDS_IN_MINUTE
MICROSECONDS_IN_HOUR = MICROSECONDS_IN_SECOND * SECONDS_IN_HOUR
MICROSECONDS_IN_DAY = MICROSECONDS_IN_SECOND * SECONDS_IN_DAY

INTERVAL_REGEX_STR = r'''
    ^
    ((?P<days>\d+)\ days?,\ )?                                 # Optional days
    (?P<hours>\d+):(?P<minutes>[0-5]?\d):(?P<seconds>[0-5]?\d) # HH:mm:ss
    (\.(?P<microseconds>\d+))?                                 # Optional microseconds
    $
'''
INTERVAL_REGEX = re.compile(INTERVAL_REGEX_STR, re.VERBOSE)
