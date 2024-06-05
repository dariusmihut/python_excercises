from setuptools import setup, find_packages

setup(
    name='trainme',
    version='1.1',
    packages=find_packages(include=['python_excercises']),
    install_requires=[
        'certifi==2024.2.2',
        'charset-normalizer==3.3.2',
        'idna',
        'requests==2.32.2',
        'urllib3==1.26.15'
    ],
    entry_points={
        'console_scripts': ['trainme=python_excercises.train:main']
    }
)
