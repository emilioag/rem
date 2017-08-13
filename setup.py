from setuptools import setup

setup(
    name='rem',
    version='0.1',
    py_modules=['rem'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        rem=script.main:main
    ''',
)