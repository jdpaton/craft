import os
from distutils.core import setup

this_path = os.path.dirname(os.path.realpath(__file__))

setup(
    name='craft',
    version='0.2.4',
    author='Jamie Paton',
    author_email='jamie.paton@googlemail.com',
    packages=['craft'],
    scripts=['bin/craft'],
    url='http://pypi.python.org/pypi/craft/',
    license='LICENSE.txt',
    description='Craft - Like Makefile, but in Python.',
    long_description=open(os.path.join(this_path,'README.pypi')).read(),
    install_requires=[
        "termcolor == 1.1.0",
    ],
)
