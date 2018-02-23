# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

#with open('LICENSE') as f:
#    license = f.read()


# *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
version = '0.0.1'


setup(
    name='eth-bot',
    version=version,
    description='Bot classes for writing dapp simulations',
    long_description=readme,
    author='Bryant Eisenbach',
    author_email='bryant@dappdevs.org',
    url='https://github.com/fubuloubu/eth-bot',
    #license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
    	'web3>=4.0.0b10'
    ]
)
