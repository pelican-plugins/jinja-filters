import codecs
import os
import re

import setuptools


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_meta(*meta_file_parts, meta_key):
    """Extract __*meta*__ from meta_file."""
    meta_file = read(*meta_file_parts)
    meta_match = re.search(r"^__{}__ = ['\"]([^'\"]*)['\"]".format(meta_key),
                           meta_file, re.M)
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{}__ string.".format(meta_key))


##############################################################################
#                          PACKAGE METADATA                                  #
##############################################################################
META_PATH = ['minchin', 'pelican', 'jinja_filters', '__init__.py']

NAME         = find_meta(*META_PATH, meta_key='title').lower()
VERSION      = find_meta(*META_PATH, meta_key='version')
SHORT_DESC   = find_meta(*META_PATH, meta_key='description')
LONG_DESC    = read('README.rst')
AUTHOR       = find_meta(*META_PATH, meta_key='author')
AUTHOR_EMAIL = find_meta(*META_PATH, meta_key='email')
URL          = find_meta(*META_PATH, meta_key='url')
LICENSE      = find_meta(*META_PATH, meta_key='license')

PACKAGES     = setuptools.find_packages()

INSTALL_REQUIRES = [
    'pelican',
    'pelican-jinja-filters >= 2.1.0',  # replacement package
]

EXTRA_REQUIRES = {
    'build': [
        'pip',
        'wheel',
        'setuptools >=18.0',
        'twine',
        'minchin.releaser >= 0.4.2',
    ],
    # 'docs': [
    #     'sphinx >= 1.3, <1.4',  # theme isssue with 1.4
    #     'cloud_sptheme >=1.6, !=1.7',  # 1.7 throws 'divide by zero'
    #     'releases',
    #     'Babel >=1.3,!=2.0',  # 2.0 breaks on Windows

    # ],
    # 'test': [
    #     'green >=1.9.4',  # v2 works
    #     'coverage',
    #     'isort',
    #     'pydocstyle',
    #     'pycodestyle',
    #     'check-manifest'
    # ],
}

NAMESPACE_PACKAGES = [
    'minchin',
    'minchin.pelican',
]

# full list of Classifiers at
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    #   having an unknown classifier should keep PyPI from accepting the
    #   package as an upload
    # 'Private :: Do Not Upload',

    # 'Development Status :: 1 - Planning',
    # 'Development Status :: 2 - Pre-Alpha',
    # 'Development Status :: 3 - Alpha',
    # 'Development Status :: 4 - Beta',
    # 'Development Status :: 5 - Production/Stable',
    # 'Development Status :: 6 - Mature',
    'Development Status :: 7 - Inactive',

    # 'Programming Language :: Python :: 2',
    # 'Programming Language :: Python :: 2.6',
    # 'Programming Language :: Python :: 2.7',
    # 'Programming Language :: Python :: 2 :: Only',
    'Programming Language :: Python :: 3',
    # 'Programming Language :: Python :: 3.2',
    # 'Programming Language :: Python :: 3.3',
    # 'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    # 'Programming Language :: Python :: 3 :: Only',

    'Environment :: Web Environment',
    'Framework :: Pelican',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Python Modules',
]
##############################################################################

if LICENSE in ['MIT License']:
    CLASSIFIERS += ['License :: OSI Approved :: {}'.format(LICENSE)]

# add 'all' key to EXTRA_REQUIRES
all_requires = []
for k, v in EXTRA_REQUIRES.items():
    all_requires.extend(v)
EXTRA_REQUIRES['all'] = all_requires


setuptools.setup(
    name=NAME,
    version=VERSION,
    url=URL,
    license=LICENSE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=SHORT_DESC,
    long_description=LONG_DESC,
    long_description_content_type="text/x-rst",
    packages=PACKAGES,
    package_data={'': ['README.rst', 'License.txt', "CHANGELOG.rst"]},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRA_REQUIRES,
    namespace_packages=NAMESPACE_PACKAGES,
    platforms='any',
    classifiers=CLASSIFIERS,
)
