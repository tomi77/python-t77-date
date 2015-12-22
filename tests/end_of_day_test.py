from datetime import datetime
import unittest

from t77_date.date import end_of_day


class EndOfDayTestCase(unittest.TestCase):
    def test_new_object(self):
        now = datetime.now()
        eod = end_of_day(now)
        self.assertNotEqual(now, eod)

    def test_now(self):
        now = datetime.now()
        eod = end_of_day(now)
        self.assertEqual(eod, datetime(now.year, now.month, now.day, 23, 59, 59, 999999))
