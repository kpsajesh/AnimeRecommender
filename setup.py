from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME-RECOMMENDER",
    version="0.1",
    author="SajeshKumar",
    packages=find_packages(),
    install_requires = requirements,
)
#Steps to run
#a. python -m venv venv
#b. venv\scripts\activate
#c.	pip install -e .
