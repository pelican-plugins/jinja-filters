from datetime import datetime
import unittest

from pelican.plugins.jinja_filters import jinja_filters


class Test_Datetime(unittest.TestCase):
    def test_basic(self):
        my_date = datetime(2016, 11, 25, 12, 34)
        assert jinja_filters.datetime(my_date) == "2016/11/25 12:34"


def main():
    unittest.main()


if __name__ == "__main__":
    main()
