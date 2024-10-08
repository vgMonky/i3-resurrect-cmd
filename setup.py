# setup.py

from setuptools import setup, find_packages

setup(
    name='i3-resurrect-cmd',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'i3ipc',
    ],
    entry_points='''
        [console_scripts]
        i3-resurrect-cmd=i3_resurrect_cmd.main:cli
    ''',
)
