"""
``Jinja Filters`` is a plugin for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

``Jinja Filters`` provides a selection of functions (called *filters*) for
templates to use when building your website. They are packaged for Pelican, but
may prove useful for other projects that make use of Jinja.
"""

import logging

from pelican import signals

from . import filters

__version__ = "1.0.0+dev.1"

logger = logging.getLogger(__name__)


def add_all_filters(pelican):
    """ Adds all filters to Pelican. """

    pelican.env.filters.update({'datetime': filters.datetime()})
    pelican.env.filters.update({'article_date': filters.article_date()})
    pelican.env.filters.update({'breaking_spaces': filters.breaking_spaces()})
    pelican.env.filters.update({'titlecase': filters.titlecase()})


def register():
    """ Plugin registration. """
    signals.generator_init.connect(add_all_filters)
