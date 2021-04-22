import unittest

from pelican.plugins.jinja_filters import jinja_filters


class Test_Titlecase(unittest.TestCase):
    def test_basic(self):
        in_text = "non-capitalized boring title"
        out_text = "Non-Capitalized Boring Title"
        assert jinja_filters.titlecase(in_text) == out_text


def main():
    unittest.main()


if __name__ == "__main__":
    main()
