# setup.py
from setuptools import setup, find_packages

setup(
    name="my_python_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest",
    ],
)