from datetime import datetime
import unittest

from t77_date.date import start_of_month


class StartOfMonthTestCase(unittest.TestCase):
    def test_new_object(self):
        now = datetime.now()
        eod = start_of_month(now)
        self.assertNotEqual(now, eod)

    def test_now(self):
        now = datetime.now()
        som = start_of_month(now)
        self.assertEqual(som, datetime(now.year, now.month, 1))
