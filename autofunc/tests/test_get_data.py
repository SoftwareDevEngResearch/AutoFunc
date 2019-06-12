
from autofunc.get_data import get_data
import pytest
import os



def test_1():

    """
    For this particular .csv file, check to make sure the first component is ic motor
    """

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../assets/bladeQueryClean.csv')

    assert get_data(file)[0][0][0] == 'ic motor'


def test_2():

    """
    For this particular .csv file, check to make sure the first function-flow is convert chemical
    """

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../assets/bladeQueryClean.csv')

    assert get_data(file)[0][1][0] == 'convert chemical'

def test_3():

    """
    For this particular .csv file, check to make sure the last component is positioner
    """

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../assets/bladeQueryClean.csv')

    assert get_data(file)[0][0][89] == 'positioner'