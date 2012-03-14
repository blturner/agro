import os
from distutils.core import setup
from setuptools import find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.markdown')

setup(
    name='agro',
    version='0.1',
    url='https://github.com/camflan/agro',
    license='BSD',
    description='Aggregates personal online activity with plug-in based architecture.',
    long_description=README,
    author='Camron Flanders',
    author_email='me@camronflanders.com',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
