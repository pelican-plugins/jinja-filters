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

__version__ = "1.0.0+dev.0"

logger = logging.getLogger(__name__)


def add_all_filters(pelican):
	""" Adds all filters to Pelican. """

	pelican.settings['JINJA_FILTERS']['datetime'] = filters.datetime
	pelican.settings['JINJA_FILTERS']['article_date'] = filters.article_date
	pelican.settings['JINJA_FILTERS']['breaking_spaces'] = filters.breaking_spaces


def register():
	""" Plugin registration. """
	signals.initialized.connect(add_all_filters)
