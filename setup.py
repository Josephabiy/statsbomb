""" Setup file for src project """
from setuptools import setup, find_packages

setup(
    name="src",
    author="Joseph Abiy",
    version="0.0.1",
    install_requires=[
        "requests==2.22.0",
        "black",
        "pytest",
        "pandas",
        "pymysql",
        "sqlalchemy",
        "cryptography",
    ],
    packages=find_packages(),
)
