from setuptools import setup, find_packages
from os.path import join, dirname

import src

setup(
    name='finiteStateMachine',
    include_package_data=True,
    version=src.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':[
            'helloworld = src.core:print_message', 
            'serve = src.web:run_server',
            ]
        },

    install_requires=[
        'Flask==0.8'    
    ]
    )
