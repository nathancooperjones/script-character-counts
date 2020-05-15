from setuptools import find_packages, setup

with open('script_character_counts/_version.py') as version_file:
    exec(version_file.read())

with open('README.md') as r:
    readme = r.read()

setup(
    name='script_character_counts',
    version=__version__,
    description="Script analysis for the Geena Davis Institute's Spell Check for Bias tool",
    long_description=readme,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
    ]
)
