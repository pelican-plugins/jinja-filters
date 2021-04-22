from datetime import datetime
import unittest

from pelican.plugins.jinja_filters import jinja_filters


class Test_Artice_Date(unittest.TestCase):
    def test_basic(self):
        my_date = datetime(2016, 11, 4, 12, 34)
        assert jinja_filters.article_date(my_date) == "Friday, November 4, 2016"


def main():
    unittest.main()


if __name__ == "__main__":
    main()
