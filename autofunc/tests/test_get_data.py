
from autofunc.get_data import get_data
import pytest
import os



def test_1():

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../assets/bladeQueryClean.csv')

    assert get_data(file)[0][0][0] == 'ic motor'


def test_2():

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../assets/bladeQueryClean.csv')

    assert get_data(file)[0][1][0] == 'convert chemical'

def test_3():

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../assets/bladeQueryClean.csv')

    assert get_data(file)[0][0][89] == 'positioner'