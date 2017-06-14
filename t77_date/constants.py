"""A set of date related constants"""
HOURS_IN_DAY = 24

MINUTES_IN_HOUR = 60
MINUTES_IN_DAY = MINUTES_IN_HOUR * HOURS_IN_DAY

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = SECONDS_IN_MINUTE * MINUTES_IN_HOUR
SECONDS_IN_DAY = SECONDS_IN_HOUR * HOURS_IN_DAY

MILLISECONDS_IN_SECOND = 1000
MILLISECONDS_IN_MINUTE = MILLISECONDS_IN_SECOND * SECONDS_IN_MINUTE
MILLISECONDS_IN_HOUR = MILLISECONDS_IN_MINUTE * MINUTES_IN_HOUR
MILLISECONDS_IN_DAY = MILLISECONDS_IN_HOUR * HOURS_IN_DAY

MICROSECONDS_IN_MILLISECONDS = 1000
MICROSECONDS_IN_SECOND = MICROSECONDS_IN_MILLISECONDS * 1000
MICROSECONDS_IN_MINUTE = MICROSECONDS_IN_SECOND * SECONDS_IN_MINUTE
MICROSECONDS_IN_HOUR = MICROSECONDS_IN_MINUTE * MINUTES_IN_HOUR
MICROSECONDS_IN_DAY = MICROSECONDS_IN_HOUR * HOURS_IN_DAY

INTERVAL_REGEX_STR = r'''
    ^
    ((?P<days>\d+)\ days?,\ )?                                 # Optional days
    (?P<hours>\d+):(?P<minutes>[0-5]?\d):(?P<seconds>[0-5]?\d) # HH:mm:ss
    (\.(?P<microseconds>\d+))?                                 # Optional microseconds
    $
'''

ISO_MONDAY = 1
ISO_TUESDAY = 2
ISO_WEDNESDAY = 3
ISO_THURSDAY = 4
ISO_FRIDAY = 5
ISO_SATURDAY = 6
ISO_SUNDAY = 7

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6
