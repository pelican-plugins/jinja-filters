import unittest

from pelican.plugins.jinja_filters import jinja_filters


class Test_Unwrap_Links(unittest.TestCase):
    def test_basic(self):
        in_text = "hello,<a href=\"about:blank\">there,<b>visitor</b></a>"
        out_text = "hello,there,<b>visitor</b></a>"
        assert jinja_filters.unwrap_links(in_text) == out_text


def main():
    unittest.main()


if __name__ == "__main__":
    main()
