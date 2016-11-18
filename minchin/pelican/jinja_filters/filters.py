"""
Various filters for Jinja.
"""

from titlecase import titlecase as _titlecase

__all__ = ['datetime',
           'article_date',
           'breaking_spaces']


def datetime(value, format='%Y/%m/%d %H:%M'):
    """
    Convert a datetime to a different format.

    The default format looks like --> 2016/11/25 12:34
    """
    return value.strftime(format)


def article_date(value):
    """
    Converts a date to the format we want it displayed on the article template.

    Format looks like --> Friday, November 4, 2016
    """
    return value.strftime('%A, %B %-d, %Y')


def breaking_spaces(value):
    """Converts non-breaking spaces to regular spaces."""
    return value.replace('\u00A0', ' ')


def titlecase(value):
    """ Returns the titlecased version of the supplied text."""
    return _titlecase(value)
