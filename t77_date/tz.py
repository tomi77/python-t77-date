"""dateutil.tz related functions"""
from __future__ import absolute_import

import re
from datetime import datetime

import dateutil.tz

TIME_ZONES_RE = re.compile(r'^(\w+)_to_(\w+)')


class TZConverter(object):
    """Convert datetime.datetime object between timezones"""

    def __call__(self, val, tzfrom, tzto):
        if not isinstance(val, datetime):
            raise ValueError('value must be a datetime.datetime object')

        if val.tzinfo is None:
            val = val.replace(tzinfo=tzfrom)

        return val.astimezone(tzto)

    def __getattr__(self, item):
        if TIME_ZONES_RE.match(item):
            time_zones = TIME_ZONES_RE.findall(item)
            tzfrom = getattr(dateutil.tz, 'tz%s' % time_zones[0][0])
            tzto = getattr(dateutil.tz, 'tz%s' % time_zones[0][1])

            if tzfrom is None:
                raise ValueError('Invalid tz "%s".' % tzfrom)
            if tzto is None:
                raise ValueError('Invalid tz "%s".' % tzto)

            return lambda val: self(val, tzfrom(), tzto())
        else:
            raise AttributeError('Invalid format "%s". Proper is "tz_to_tz".' % item)


tzconverter = TZConverter()
