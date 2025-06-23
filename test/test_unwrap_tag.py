import unittest

from pelican.plugins.jinja_filters import jinja_filters


class Test_Unwrap_Tag(unittest.TestCase):
    def test_basic(self):
        in_text = "hello,<a href=\"about:blank\">there,<b>visitor</b></a>"
        in_text = "hello,<a href=\"about:blank\">there,visitor</a>"
        tag_name = "b"
        assert jinja_filters.unwrap_tag(in_text,tag_name) == out_text


def main():
    unittest.main()


if __name__ == "__main__":
    main()
