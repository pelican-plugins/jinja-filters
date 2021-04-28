import unittest

from pelican.plugins.jinja_filters import jinja_filters


class Test_Breaking_Spaces(unittest.TestCase):
    def test_basic(self):
        in_text = "Break\u00A0Everything!"
        out_text = "Break Everything!"
        assert jinja_filters.breaking_spaces(in_text) == out_text


def main():
    unittest.main()


if __name__ == "__main__":
    main()
