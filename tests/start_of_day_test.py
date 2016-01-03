from datetime import datetime
import unittest

from t77_date.t77_datetime import start_of_day


class StartOfDayTestCase(unittest.TestCase):
    def test_new_object(self):
        """start_of_day create a new object"""
        now = datetime.now()
        eod = start_of_day(now)
        self.assertNotEqual(now, eod)

    def test_now(self):
        """Beginning of day at 00:00:00"""
        now = datetime.now()
        sod = start_of_day(now)
        self.assertEqual(sod, datetime(now.year, now.month, now.day))
