=============
Jinja Filters
=============

``Jinja Filters`` is a plugin for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

``Jinja Filters`` provides a selection of functions (called *filters*) for
templates to use when building your website. They are packaged for Pelican, but
may prove useful for other projects that make use of
`Jinja2 <http://jinja.pocoo.org/>`_.


Installation
============

The easiest way to install ``Jinja Filters`` is through the use of pip. This
will also install the required dependencies (currently none) automatically.

.. code-block:: sh

  pip install minchin.pelican.jinja_filters

Then, in your ``pelicanconf.py`` file, add ``Jinja Filters`` to your list of
plugins:

.. code-block:: python

  PLUGINS = [
              # ...
              'minchin.pelican.jinja_filters',
              # ...
            ]

And that's it! The filters are now available for use in your templates.


Usage
=====

At present, the plugin includes the following filters:

- ``datetime`` |--| allows you to change to format displayed for a datetime
  object. Optionally supply a `datetime format string
  <https://docs.python.org/3.6/library/datetime.html#strftime-and-strptime-behavior>`_
  to get a custom format.
- ``article_date`` |--| a specialized version of ``datetime`` that returns
  datetimes as wanted for article dates; speciefically
  *Friday, November 4, 2016*.
- ``breaking_spaces`` |--| replaceds non-breaking spaces (HTML code *&nbsp*)
  with normal spaces.

For example, within your theme templates, you might have code like:

.. code-block:: html+jinja2

    <span class="published">
        Article Published {{ article.date | article_date }}
    </span>

gives::
    
    Article Published Friday, November 4, 2016

Or with your own dateformat:

.. code-block:: html+jinja2

    <span class="published">
        Article Published {{ article.date | datetime('%b %d, %Y') }}
    </span>

gives::

    Article Published Nov 04, 2016

To remove breaking spaces, you might have code like:

.. code-block:: html+jinja2

    <a href="{{ SITEURL }}/{{ article.category.url }}">
        {{ article.category | breaking_spaces}}
    </a>


.. |--| unicode:: U+2013   .. en dash
