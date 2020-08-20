"""Various filters for Jinja."""

from titlecase import titlecase as _titlecase

__all__ = ["datetime", "article_date", "breaking_spaces", "titlecase"]


def datetime(value, format_str="%Y/%m/%d %H:%M"):
    """
    Convert a datetime to a different format.

    The default format looks like --> 2016/11/25 12:34

    Args:
        value (datetime.datetime): input date and time
        format_str (str): The datetime format string to apply to value

    Returns:
        str: value, after the format_str has been applied
    """
    return value.strftime(format_str)


def article_date(value):
    """
    Convert a date to the format we want it displayed on the article template.

    Format looks like --> Friday, November 4, 2020

    Args:
        value (datetime.datetime): input date

    Returns:
        str: value, formatted nicely for displaying the date.
    """
    return value.strftime("%A, %B %-d, %Y")


def breaking_spaces(value):
    """
    Convert non-breaking spaces to regular spaces.

    Args:
        value (str): input value

    Returns:
        str: the input string, now with regular spaces
    """
    return value.replace("\u00A0", " ")


def titlecase(value):
    """Returns the titlecased version of the supplied text.

    Args:
        value (str): input value

    Returns:
        str: value, titlecase formatted
    """
    return _titlecase(value)
