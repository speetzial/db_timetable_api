from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Simple access to the Deutsche Bahn timetable API'

# Setting up
setup(
    name="db_timetable_api",
    version=VERSION,
    author="Sebastian Speetzen",
    author_email="<sebastianspeetzen@googlemail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'api', 'trains', 'db', 'deutsche bahn', 'fahrplan', 'timetable api', 'timetable', 'train timetable', 'train timetable api', 'train timetable api', 'train timetable', 'train', 'trains', 'train station', 'train stations', 'train station api', 'train station timetable', 'train station timetable api', 'train station timetable api', 'train station timetable', 'train station', 'train stations', 'train station api', 'train station timetable', 'train station timetable api', 'train station timetable api', 'train station timetable', 'train station', 'train stations', 'train station api', 'train station timetable', 'train station timetable api', 'train station timetable api', 'train station timetable', 'train station', 'train stations', 'train station api', 'train station timetable', 'train station timetable api', 'train station timetable api', 'train station timetable', 'train station', 'train stations', 'train station api', 'train station timetable', 'train station timetable api', 'train station timetable api', 'train station timetable', 'train station', 'train stations', 'train station api', 'train station timetable', 'train station timetable api', 'train station timetable api', 'train station timetable', 'train station', 'train stations', 'train station api', 'train station timetable', 'train station timetable api', 'train station timetable api', 'train station timetable', 'train station', 'train stations', 'train station api', 'train station timetable', 'train station timetable api', 'train station timetable api', 'train station timetable', 'train station', 'train stations', 'train station api', 'train station timetable', 'train station timetable api', 'train station timetable api', 'train station timetable', 'train station', 'train stations', 'train station api', 'train station timetable', 'train station timetable api', 'train station timetable api', 'train station timetable', 'train station', 'train stations', 'train station api', 'train station timetable', 'train station timetable api'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)