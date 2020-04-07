from setuptools import setup, find_packages

from channels_handlers import __version__


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="django-channels-handlers",
    version=__version__,
    url="https://github.com/joshua-s/django-channels-handlers",
    author="Josh Smith",
    author_email="josh@joshsmith.codes",
    license="MIT",
    description="Django Channels, without the Pain 💊",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.6",
    install_requires=["Django>=2.1", "channels>=2.2", "pydantic~=1.4"],
    include_package_data=True,
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
        "Framework :: Django :: 3.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
    ],
)
