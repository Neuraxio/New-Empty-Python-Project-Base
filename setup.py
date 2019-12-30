"""
This files originate from the "New-Empty-Python-Project-Base" template:
    https://github.com/Neuraxio/New-Empty-Python-Project-Base 
Created by Guillaume Chevalier at Neuraxio:
    https://github.com/Neuraxio 
    https://github.com/guillaume-chevalier 
License: CC0-1.0 (Public Domain)
"""

from setuptools import setup, find_packages

with open('README.md') as _f:
    _README_MD = _f.read()

_VERSION = '0.1'

setup(
    name='project', # TODO: rename. 
    version=_VERSION,
    description='An empty project base.',
    long_description=_README_MD,
    classifiers=[
        # TODO: typing.
        "Typing :: Typed"
    ],
    url='https://github.com/..../....',  # TODO.
    download_url='https://github.com/.../.../tarball/{}'.format(_VERSION),  # TODO.
    author='Neuraxio Inc.',  # TODO.
    author_email='guillaume.chevalier@neuraxio.com',  # TODO.
    packages=find_packages(include=['project*']),  # TODO.
    test_suite="testing",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    install_requires=["neuraxle"],
    include_package_data=True,
    license='TODO',  # TODO: set your license string. 
    keywords='empty project TODO keywords'
)

