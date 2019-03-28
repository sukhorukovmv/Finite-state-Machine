from setuptools import setup, find_packages
from os.path import join, dirname

import src

setup(
    name='finiteStateMachine', # name project for search in PyPI "pip install finiteStateMachine"
    include_package_data=True,
    version=src.__version__,
    setup_requires=[], # all libraries on which the build depends
    tests_require=[], # all libraries on which the run tests depends
    packages=find_packages(), #(exclude=[".tests.*, .templates.*"]),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':[
            'helloworld = src.core:print_message', 
            'serve = src.web:run_server',
        ]
    },

    package_data={  # all files on which include in the final package
    '': [
        './test/*.py', 
        'README.md', 
        '*.png',
        'MANIFEST.in',
        ],
    },

    install_requires=[ # all libraries on which the package depends, except standart library
        'Flask'    
    ]
)
#$ python -m unittest discover

