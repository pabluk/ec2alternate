from setuptools import setup

setup(
    name='ec2alternate',
    version='0.1',
    author='Pablo SEMINARIO',
    author_email='pabluk@gmail.com',
    description=("A simple command to alternate two EC2 instances."),
    url='https://github.com/pabluk/ec2alternate',
    packages=['ec2alternate'],

    entry_points={
        'console_scripts': ['ec2alternate = ec2alternate.main:main']
    },
    install_requires=['boto >= 2.0'],
)
