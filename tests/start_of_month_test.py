from datetime import datetime, date
import unittest

from t77_date.datetime import start_of_month


class StartOfMonthTestCase(unittest.TestCase):
    def test_new_object(self):
        """start_of_month create a new object"""
        now = datetime.now()
        som = start_of_month(now)
        self.assertNotEqual(now, som)

    def test_now(self):
        """Beginning of month at 00:00:00 1st day"""
        now = datetime.now()
        som = start_of_month(now)
        self.assertEqual(som, datetime(now.year, now.month, 1))

    def test_date(self):
        now = date.today()
        som = start_of_month(now)
        self.assertEqual(som, datetime(now.year, now.month, 1))
