from setuptools import setup
setup(
    name = 'serverlist_CLI',
    version = '0.1.0',
    packages = ['serverlist'],
    entry_points = {
        'console_scripts': [
            'serverlist = serverlist.__main__:main'
        ]
    })
