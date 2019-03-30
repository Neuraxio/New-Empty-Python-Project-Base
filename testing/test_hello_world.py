"""
This files originate from the "New-Empty-Python-Project-Base" template:
    https://github.com/Neuraxio/New-Empty-Python-Project-Base 
Created by Guillaume Chevalier at Neuraxio:
    https://github.com/Neuraxio 
    https://github.com/guillaume-chevalier 
License: CC0-1.0 (Public Domain)
"""

import pytest

from project.hello_world import hello_world

@pytest.mark.parametrize("argument_values", [True, 1, 1.0])
def test_example(argument_values):
    assert True == argument_values

def test_hello_world(): 
    assert hello_world() == "Hello World!"

