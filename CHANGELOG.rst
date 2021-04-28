Jinja Filters Changelog
=======================

2.1.0 - 2021-04-28
------------------

- **feature** add ``merge_date_url`` filter. See `Pull Request #12`_.
- **feature** add ``datetime_from_period`` filter. `Pull Request #12`_.
- **support** rework supporting ``tasks.py`` (for use with ``invoke``). See
  `Pull Request #8`_.
- **support** add test suite
- **support** support Pelican from version 3.0 on. See `Pull Request #10`_.

.. _Pull Request #8: https://github.com/pelican-plugins/jinja-filters/pull/8
.. _Pull Request #10: https://github.com/pelican-plugins/jinja-filters/pull/10
.. _Pull Request #12: https://github.com/pelican-plugins/jinja-filters/pull/12

2.0.0 - 2020-08-21
------------------

- **feature** Initial release as namespace plugin. With Pelican 4.5,
  namespace plugins no longer need to be explicitly declared to be available to
  Pelican.
- **support** minimum version of Pelican is now 4.5
- **support** Move plugin to the `Pelican Plugins`_ organization on GitHub. The
  code for the project is now at `pelican-plugins/jinja-filters`_
- **support** first release to PyPI under `pelican-jinja-filters`_
- see `Pull Request #4`_.

1.0.4 - 2017-04-17
------------------

- **bug** upgrade release machinery
- **bug** add Pelican trove classifier

1.0.1 - 2017-03-08
------------------

- **bug** provide universal wheels

1.0.0 - 2016-11-06
------------------

- **feature** copy existing code from personal website
- **support** add release machinery
- **support** first release to PyPI under `minchin.pelican.jinja_filters`_
- **support** add 'setup.py', 'CHANGELOG.rst', 'README.rst'


.. _minchin.pelican.jinja_filters: https://pypi.org/project/minchin.pelican.jinja_filters/
.. _pelican-plugins/jinja-filters: https://github.com/pelican-plugins/jinja-filters
.. _pelican-jinja-filters: https://pypi.org/project/pelican-jinja-filters/
.. _Pelican Plugins: https://github.com/pelican-plugins
.. _Pull Request #4: https://github.com/pelican-plugins/jinja-filters/pull/4
