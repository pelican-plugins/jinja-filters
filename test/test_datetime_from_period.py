from datetime import datetime
import unittest

from pelican.plugins.jinja_filters import jinja_filters


class Test_Datetime_From_Period(unittest.TestCase):
    def test_year_period(self):
        period = (2021,)
        expected_date = datetime(2021, 1, 1)
        assert jinja_filters.datetime_from_period(period) == expected_date

    def test_month_period(self):
        period = (2021, "April")
        expected_date = datetime(2021, 4, 1)
        assert jinja_filters.datetime_from_period(period) == expected_date

    def test_day_period(self):
        period = (2021, "April", 21)
        expected_date = datetime(2021, 4, 21)
        assert jinja_filters.datetime_from_period(period) == expected_date

    def test_int_month_period(self):
        period = (2021, 4)
        expected_date = datetime(2021, 4, 1)
        assert jinja_filters.datetime_from_period(period) == expected_date

    def test_int_day_period(self):
        period = (2021, 4, 21)
        expected_date = datetime(2021, 4, 21)
        assert jinja_filters.datetime_from_period(period) == expected_date

    def test_single_digit_day(self):
        period = (2021, "April", 3)
        expected_date = datetime(2021, 4, 3)
        assert jinja_filters.datetime_from_period(period) == expected_date

    def test_bare_year_period(self):
        period = 2021
        expected_date = datetime(2021, 1, 1)
        assert jinja_filters.datetime_from_period(period) == expected_date


def main():
    unittest.main()


if __name__ == "__main__":
    main()
