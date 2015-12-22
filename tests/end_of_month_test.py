from datetime import datetime
import unittest

from t77_date.date import end_of_month


class EndOfMonthTestCase(unittest.TestCase):
    def test_new_object(self):
        now = datetime.now()
        eod = end_of_month(now)
        self.assertNotEqual(now, eod)

    def test_january(self):
        january = datetime(2015, 1, 6, 12, 45, 23, 123)
        eom = end_of_month(january)
        self.assertEqual(eom, datetime(2015, 1, 31, 23, 59, 59, 999999))

    def test_february(self):
        february = datetime(2015, 2, 6, 12, 45, 23, 123)
        eom = end_of_month(february)
        self.assertEqual(eom, datetime(2015, 2, 28, 23, 59, 59, 999999))

    def test_february_leap(self):
        february = datetime(2000, 2, 6, 12, 45, 23, 123)
        eom = end_of_month(february)
        self.assertEqual(eom, datetime(2000, 2, 29, 23, 59, 59, 999999))

    def test_march(self):
        march = datetime(2015, 3, 6, 12, 45, 23, 123)
        eom = end_of_month(march)
        self.assertEqual(eom, datetime(2015, 3, 31, 23, 59, 59, 999999))

    def test_april(self):
        april = datetime(2015, 4, 6, 12, 45, 23, 123)
        eom = end_of_month(april)
        self.assertEqual(eom, datetime(2015, 4, 30, 23, 59, 59, 999999))

    def test_may(self):
        may = datetime(2015, 5, 6, 12, 45, 23, 123)
        eom = end_of_month(may)
        self.assertEqual(eom, datetime(2015, 5, 31, 23, 59, 59, 999999))

    def test_june(self):
        june = datetime(2015, 6, 6, 12, 45, 23, 123)
        eom = end_of_month(june)
        self.assertEqual(eom, datetime(2015, 6, 30, 23, 59, 59, 999999))

    def test_july(self):
        july = datetime(2015, 7, 6, 12, 45, 23, 123)
        eom = end_of_month(july)
        self.assertEqual(eom, datetime(2015, 7, 31, 23, 59, 59, 999999))

    def test_august(self):
        august = datetime(2015, 8, 6, 12, 45, 23, 123)
        eom = end_of_month(august)
        self.assertEqual(eom, datetime(2015, 8, 31, 23, 59, 59, 999999))

    def test_september(self):
        september = datetime(2015, 9, 6, 12, 45, 23, 123)
        eom = end_of_month(september)
        self.assertEqual(eom, datetime(2015, 9, 30, 23, 59, 59, 999999))

    def test_october(self):
        october = datetime(2015, 10, 6, 12, 45, 23, 123)
        eom = end_of_month(october)
        self.assertEqual(eom, datetime(2015, 10, 31, 23, 59, 59, 999999))

    def test_november(self):
        november = datetime(2015, 11, 6, 12, 45, 23, 123)
        eom = end_of_month(november)
        self.assertEqual(eom, datetime(2015, 11, 30, 23, 59, 59, 999999))

    def test_december(self):
        december = datetime(2015, 12, 6, 12, 45, 23, 123)
        eom = end_of_month(december)
        self.assertEqual(eom, datetime(2015, 12, 31, 23, 59, 59, 999999))
