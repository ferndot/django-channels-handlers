import io
import os
import re

from setuptools import find_packages
from setuptools import setup

from channels_handlers import __version__


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type("")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


setup(
    name="channels_handlers",
    version=__version__,
    url="https://github.com/joshua-s/django-channels-handlers",
    license="MIT",
    author="Josh Smith",
    author_email="josh@joshsmith.codes",
    description="Django Channels, without the Pain 💊",
    long_description=read("README.rst"),
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.5",
    install_requires=["Django>=2.1", "channels~=2.2"],
    extras_require={
        "tests": [
            "pytest~=5.0",
            "pytest-django~=3.5",
            "pytest-asyncio~=0.10",
            "pytest-cov>=2.7",
            "black>=19.3b0",
            "flake8>=3.7",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Framework :: Django",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
    ],
)
