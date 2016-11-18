
import os
import re
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

base_dir = os.path.dirname(os.path.abspath(__file__))


def get_version(filename="minchin/pelican/plugins/cname.py"):
    with open(os.path.join(base_dir, filename), encoding="utf-8") as initfile:
        for line in initfile.readlines():
            m = re.match("__version__ *= *['\"](.*)['\"]", line)
            if m:
                return m.group(1)


setup(
    name="minchin.pelican.jinja_filters",
    version=get_version(),
    description="Jinja filters for Pelican.",
    long_description="\n\n".join([open(os.path.join(base_dir, "README.rst")).read()]),
    author="W. Minchin",
    author_email="w_minchin@hotmail.com",
    url="https://github.com/MinchinWeb/minchin.pelican.jinja_filters",
    packages=find_packages(),
    namespace_packages=['minchin',
                        'minchin.pelican',],
    include_package_data=True,
    install_requires=[
        'pelican',
        'titlecase',
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
)
