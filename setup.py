import os
import sys

from setuptools import find_packages
from setuptools import setup

version = "1.0.1"

install_requires = [
    "requests>=2.25.1",
    "setuptools>=41.6.0",
]

install_requires.extend(
    [
        # We specify the minimum acme and certbot version as the current plugin
        # version for simplicity. See
        # https://github.com/certbot/certbot/issues/8761 for more info.
        f"acme>={version}",
        f"certbot>={version}",
    ]
)


# Load readme to use on PyPI
with open("README.md", encoding="utf8") as f:
    readme = f.read()

setup(
    name="certbot-mdns",
    version=version,
    description="mDNS Authenticator plugin for Certbot",
    url="https://github.com/ilupasco/certbot-mdns",
    author="iLupasco",
    author_email="master@dns.md",
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Security",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        "certbot.plugins": [
            "mdns = mdns.mdns:Authenticator",
        ],
    },
)
