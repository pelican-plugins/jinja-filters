"""Various filters for Jinja."""

from datetime import datetime as _datetime

from titlecase import titlecase as _titlecase

__all__ = [
    "article_date",
    "breaking_spaces",
    "datetime",
    "titlecase",
]


def datetime(value, format_str="%Y/%m/%d %H:%M"):
    """
    Convert a datetime to a different format.

    The default format looks like --> 2016/11/25 12:34

    Args
    ----
        value (datetime.datetime): input date and time
        format_str (str): The datetime format string to apply to value

    Returns
    -------
        str: value, after the format_str has been applied

    """
    return value.strftime(format_str)


def article_date(value):
    """
    Convert a date to the format we want it displayed on the article template.

    Format looks like --> Friday, November 4, 2020

    Args
    ----
        value (datetime.datetime): input date

    Returns
    -------
        str: value, formatted nicely for displaying the date.

    """
    return value.strftime("%A, %B %-d, %Y")


def datetime_from_period(value):
    """
    Converts "period" into a datetime object.

    On yearly/monthly/daily archive pages, a "period" object is supplied so you
    know what timeperiod the particular archive page is for. This converts it
    to a datetime.datetime object, so it can be further processed.

    If a month is not provided (i.e. the period is for a yearly archive),
    January is assumed. If a day is not provided (i.e. the period is for a
    yearly or monthly archive), the 1st is assumed.

    Args
    ----
        value (tuple): input period

    Returns
    -------
        datetime.datetime: value converted

    """
    JANUARY = _datetime(2021, 1, 1).strftime("%B")
    new_value = " ".join(
        value[0],
        value[1] if len(value) > 1 else JANUARY,
        value[2] if len(value) > 2 else 1,
    )
    new_datetime = _datetime.strptime(*new_value, "%Y %B %-d")
    return new_datetime


def breaking_spaces(value):
    """
    Convert non-breaking spaces to regular spaces.

    Args
    ----
        value (str): input value

    Returns
    -------
        str: the input string, now with regular spaces

    """
    return value.replace("\u00A0", " ")


def titlecase(value):
    """
    Returns the titlecased version of the supplied text.

    Args
    ----
        value (str): input value

    Returns
    -------
        str: value, titlecase formatted

    """
    return _titlecase(value)
