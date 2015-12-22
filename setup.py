import codecs
import os

from setuptools import setup, find_packages


def read(filepath):
    filepath = os.path.join(os.path.dirname(__file__), filepath)
    return codecs.open(filepath, 'r', 'utf-8').read()

description = read('README.md')

setup(
    name="t77-date",
    version='0.1',
    description='',
    long_description=description,
    author="Tomasz Jakub Rup",
    author_email="tomasz.rup@gmail.com",
    license='MIT',
    url='https://github.com/tomi77/python-t77-date',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
    ],
    zip_safe=False,
    test_suite="tests",
)
