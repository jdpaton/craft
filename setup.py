from distutils.core import setup

setup(
    name='craft',
    version='0.2.0',
    author='Jamie Paton',
    author_email='jamie.paton@googlemail.com',
    packages=['craft'],
    scripts=['bin/craft'],
    url='http://pypi.python.org/pypi/craft/',
    license='LICENSE.txt',
    description='Craft - Like Makefile, but in Python.',
    long_description=open('README.pypi').read(),
    install_requires=[
        "termcolor == 1.1.0",
    ],
)
