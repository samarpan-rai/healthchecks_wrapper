#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = []

test_requirements = [
    "pytest>=3.6",
]

setup(
    author="Samarpan Rai",
    author_email="samarpan-rai@live.com",
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
    ],
    description="Context manager around service provided by HealthChecks for easy use",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="healthchecks_context_manager",
    name="healthchecks_wrapper",
    packages=find_packages(include=["healthchecks_wrapper", "healthchecks_wrapper.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/samarpan-rai/healthchecks_wrapper",
    version="0.1.6",
    zip_safe=False,
)
