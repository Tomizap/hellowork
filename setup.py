from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = "0.0.1"
DESCRIPTION = """
Simple Python Package
"""

setup(
    name="hellowork",
    version=VERSION,
    author="TZ",
    author_email="zaptom.pro@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'selenium',
        'selenium_driver @ git+https://github.com/Tomizap/selenium_driver#egg=selenium_driver'],
    keywords=[],
    classifiers=[]
)
