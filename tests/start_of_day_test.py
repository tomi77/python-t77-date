from datetime import datetime
import unittest

from t77_date.date import start_of_day


class StartOfDayTestCase(unittest.TestCase):
    def test_new_object(self):
        now = datetime.now()
        eod = start_of_day(now)
        self.assertNotEqual(now, eod)

    def test_now(self):
        now = datetime.now()
        sod = start_of_day(now)
        self.assertEqual(sod, datetime(now.year, now.month, now.day))
