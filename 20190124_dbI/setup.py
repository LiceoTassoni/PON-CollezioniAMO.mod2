# vim:fileencoding=utf-8

from setuptools import setup, find_packages

setup(
    name="dbcolza",
    version="0.0.1",
    packages=find_packages(),
    license="MIT",
    package_data={'': ['static/*']},
    entry_points={
        'console_scripts': [
            'dbcolza = dbcolza.app:wsgiserver'
        ],
    },
    install_requires=[
        "flask",
        "flask-cors"#,
#        "couchdb"
    ]
)
