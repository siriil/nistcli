from setuptools import setup

setup(
    name='nistcli',
    version='0.1.0',
    py_modules=['nistcli'],
    install_requires=[
        'requests',
        'prettytable',
    ],
    entry_points={
        'console_scripts': [
            'nistcli = nistcli:main',
        ],
    },
)
