"""Packaging settings."""

from setuptools import find_packages, setup

setup(
    name="tap-matomo",
    version="0.1.0",
    description="A tap for matomo analytics.",
    url="https://github.com/epappas/tap-matomo",
    author="Evangelos Pappas",
    author_email="epappas@evalonlabs.com",
    license="Copyright (C) Evangelos Pappas - All Rights Reserved",
    keywords="signer, tap, data, analytics",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Natural Language :: English",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
    zip_safe=False,
    package_data={".": ["*.py"]},
    packages=[
        ".",
        *find_packages(exclude=["tests*", "examples", "docs", "contrib", "data"]),
    ],
    entry_points={
        "console_scripts": [
            "tap-matomo=tap_matomo.tap:cli",
        ],
    },
)
