=============
Jinja Filters
=============

|build| |pypi|

.. |build| image:: https://img.shields.io/github/workflow/status/pelican-plugins/jinja-filters/build
    :target: https://github.com/pelican-plugins/jinja-filters/actions
    :alt: Build Status

.. |pypi| image:: https://img.shields.io/pypi/v/pelican-jinja-filters.svg
    :target: https://pypi.python.org/pypi/pelican-jinja-filters
    :alt: PyPI Version

``Jinja Filters`` is a plugin for `Pelican <https://docs.getpelican.com/>`_,
a static site generator written in Python.

``Jinja Filters`` provides a selection of functions (called *filters*) for
templates to use when building your website. They are packaged for Pelican, but
may prove useful for other projects that make use of
`Jinja2 <https://palletsprojects.com/p/jinja/>`_.


Installation
============

The easiest way to install ``Jinja Filters`` is through the use of Pip. This
will also install the required dependencies (currently ``pelican`` and
``titlecase``) automatically.

.. code-block:: sh

  pip install pelican-jinja-filters

As ``Jinja Filters`` is a namespace plugin, it should automatically be loaded
by Pelican. And that's it! The filters are now available for use in your
templates.


Usage
=====

At present, the plugin includes the following filters:

- ``datetime`` |--| allows you to change to format displayed for a datetime
  object. Optionally supply a `datetime format string
  <https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-behavior>`_
  to get a custom format.
- ``article_date`` |--| a specialized version of ``datetime`` that returns
  datetimes as wanted for article dates; specifically
  *Friday, November 4, 2020*.
- ``breaking_spaces`` |--| replaces non-breaking spaces (HTML code *&nbsp*)
  with normal spaces.
- ``titlecase`` |--| Titlecases the supplied string.

For example, within your theme templates, you might have code like:

.. code-block:: html+jinja

    <span class="published">
        Article Published {{ article.date | article_date }}
    </span>

gives::

    Article Published Friday, November 4, 2020

Or with your own date format:

.. code-block:: html+jinja

    <span class="published">
        Article Published {{ article.date | datetime('%b %d, %Y') }}
    </span>

gives::

    Article Published Nov 04, 2020

Filters can also be chained, or applied in sequence. For example to remove
breaking spaces and then titlecase a category name, you might have code like:

.. code-block:: html+jinja

    <a href="{{ SITEURL }}/{{ article.category.url }}">
        {{ article.category | breaking_spaces | titlecase}}
    </a>


License
=======

``Jinja Filters`` is under the MIT License. See attached ``License.txt`` for
full license text.


.. |--| unicode:: U+2013   .. en dash
