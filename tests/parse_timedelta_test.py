import unittest
from datetime import timedelta, datetime

from t77_date.timedelta import parse_timedelta


class ParseTimedeltaTestCase(unittest.TestCase):
    def test_none(self):
        """parse_timedelta return None for None input"""
        self.assertIsNone(parse_timedelta(None))

    def test_not_str(self):
        """parse_timedelta throw TypeError when value is not str"""
        with self.assertRaises(TypeError):
            parse_timedelta([])
        with self.assertRaises(TypeError):
            parse_timedelta({})
        with self.assertRaises(TypeError):
            parse_timedelta(object())
        with self.assertRaises(TypeError):
            parse_timedelta(12)
        with self.assertRaises(TypeError):
            parse_timedelta(datetime.now())

    def test_incorrect(self):
        """parse_timedelta throw ValueError when value is invalid timedelta"""
        with self.assertRaises(ValueError):
            parse_timedelta('invalid timedelta')

    def test_hours_wo_day(self):
        self.assertEqual(parse_timedelta('1:11:12'), timedelta(hours=1, minutes=11, seconds=12))
        self.assertEqual(parse_timedelta('10:11:12'), timedelta(hours=10, minutes=11, seconds=12))
        self.assertEqual(parse_timedelta('25:11:12'), timedelta(days=1, hours=1, minutes=11, seconds=12))

    def test_hours_and_days(self):
        self.assertEqual(parse_timedelta('1 day, 10:11:12'), timedelta(days=1, hours=10, minutes=11, seconds=12))
        self.assertEqual(parse_timedelta('2 days, 10:11:12'), timedelta(days=2, hours=10, minutes=11, seconds=12))
