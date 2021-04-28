import unittest

from pelican.plugins import jinja_filters


class Test_Setup(unittest.TestCase):
    def test_we_are_live(self):
        """Test we should *always* pass"""
        pass

    def test_version(self):
        """Version is available"""
        self.assertIsNotNone(jinja_filters.__version__)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
