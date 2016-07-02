from datetime import datetime, date
import unittest

from t77_date.constants import ISO_FRIDAY
from t77_date.datetime import set_prev_iso_week_day


class SetNextISOWeekDayTestCase(unittest.TestCase):
    def test_date_saturday_to_prev_friday(self):
        saturday = date(2016, 7, 2)  # SATURDAY
        prev_friday = set_prev_iso_week_day(saturday, ISO_FRIDAY)
        self.assertEqual(prev_friday.isoweekday(), ISO_FRIDAY)
        self.assertLess(prev_friday, saturday)

    def test_date_friday_to_friday(self):
        friday = date(2016, 7, 1)  # FRIDAY
        prev_friday = set_prev_iso_week_day(friday, ISO_FRIDAY)
        self.assertEqual(prev_friday.isoweekday(), ISO_FRIDAY)
        self.assertEqual(prev_friday, friday)

    def test_date_thursday_to_prev_friday(self):
        thursday = date(2016, 6, 30)  # THURSDAY
        prev_friday = set_prev_iso_week_day(thursday, ISO_FRIDAY)
        self.assertEqual(prev_friday.isoweekday(), ISO_FRIDAY)
        self.assertLess(prev_friday, thursday)

    def test_datetime_saturday_to_prev_friday(self):
        saturday = datetime(2016, 7, 2, 12)  # SATURDAY
        prev_friday = set_prev_iso_week_day(saturday, ISO_FRIDAY)
        self.assertEqual(prev_friday.isoweekday(), ISO_FRIDAY)
        self.assertLess(prev_friday, saturday)

    def test_datetime_friday_to_friday(self):
        friday = datetime(2016, 7, 1, 12)  # FRIDAY
        prev_friday = set_prev_iso_week_day(friday, ISO_FRIDAY)
        self.assertEqual(prev_friday.isoweekday(), ISO_FRIDAY)
        self.assertEqual(prev_friday, friday)

    def test_datetime_thursday_to_prev_friday(self):
        thursday = datetime(2016, 6, 30, 12)  # THURSDAY
        prev_friday = set_prev_iso_week_day(thursday, ISO_FRIDAY)
        self.assertEqual(prev_friday.isoweekday(), ISO_FRIDAY)
        self.assertLess(prev_friday, thursday)
