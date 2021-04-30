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

As ``Jinja Filters`` is a namespace plugin, assuming you are using Pelican 4.5
(or newer) **and** *only* other namespace plugins, ``Jinja Filters`` will be
automatically be loaded by Pelican. And that's it!

If you are using an older version of Pelican, or non-namespace plugins, you may
need to add ``Jinja Filters`` to your ``pelicanconf.py``:

.. code-block:: python

  PLUGINS = [
      # others...
      "pelican.plugins.jinja_filters",
  ]

The filters are now available for use in your templates.

``Jinja Filters`` supports Pelican from version 3 on.


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
- ``breaking_spaces`` |--| replaces non-breaking spaces (HTML code *&nbsp;*)
  with normal spaces.
- ``titlecase`` |--| Titlecases the supplied string.
- ``datetime_from_period`` |--| take the ``period`` provided on period archive
  pages, and turn it into a proper datetime.datetime object (likely to feed to
  another filter)
- ``merge_date_url`` |--| given a datetime (on the left) and a supplied URL,
  "apply" the date to it. Envisioned in particular for ``YEAR_ARCHIVE_URL``,
  ``MONTH_ARCHIVE_URL``, and ``DAY_ARCHIVE_URL``.

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

    <a href="{{ SITEURL -}} / {{- article.category.url }}">
        {{ article.category | breaking_spaces | titlecase }}
    </a>

On a Monthly Archive page, you might have the following to link "up" to the
Yearly Archive page:

.. code-block:: html+jinja

    <a href="{{ SITEURL -}} /
             {{- period | datetime_from_period | merge_date_url(YEAR_ARCHIVE_URL) }}">
        {{ period | datetime_from_period | datetime('%Y') }}
    </a>

which might give::

    <a href="https://blog.minchin.ca/posts/2017/>2017</a>


Contributing
============

Contributions are most welcome! See `Contributing`_ for more details.

To set up a development environment:

1. Fork the project on GitHub, and then clone your fork.
2. Set up and activate a virtual environment.
3. Have ``invoke`` on your system path or install it into your virtual
   environment.
4. Run ``invoke setup``.

For more details, see `Contributing`_.


License
=======

``Jinja Filters`` is under the MIT License. See attached `License.txt`_ for
full license text.


.. |--| unicode:: U+2013   .. en dash
.. _Contributing: https://github.com/pelican-plugins/jinja-filters/blob/master/CONTRIBUTING.md
.. _License.txt: https://github.com/pelican-plugins/jinja-filters/blob/master/LICENSE.txt
