import unittest
from datetime import datetime

from dateutil.tz import tzutc, tzlocal

from t77_date.tz import local_to_utc


class LocalToUtcTestCase(unittest.TestCase):
    def test_datetime_in_utc(self):
        value_in = datetime.now(tz=tzutc())
        value_out = local_to_utc(value_in)
        self.assertIsInstance(value_out, datetime)
        self.assertEqual(value_out.tzinfo, tzutc())
        self.assertEqual(value_out, value_in)

    def test_datetime_in_local(self):
        value_in = datetime.now(tz=tzlocal())
        value_out = local_to_utc(value_in)
        self.assertIsInstance(value_out, datetime)
        self.assertEqual(value_out.tzinfo, tzutc())

    def test_datetime_without_tzinfo(self):
        value_in = datetime.now()
        value_out = local_to_utc(value_in)
        self.assertIsInstance(value_out, datetime)
        self.assertEqual(value_out.tzinfo, tzutc())

    def test_invalid_input(self):
        now = datetime.now()
        with self.assertRaises(ValueError):
            local_to_utc(None)
        with self.assertRaises(ValueError):
            local_to_utc(now.toordinal())
        with self.assertRaises(ValueError):
            local_to_utc(now.isoformat())
