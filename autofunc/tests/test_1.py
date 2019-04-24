
from autofunc.get_data import get_data
import pytest
import sys
import os



def test_1():
    # sys.path.append('/assets')

    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../assets/bladeQueryClean.csv')

    # store_data, records = get_data(file)

    # print(store_data)

    # print(get_data(file)[0][0][0])
    assert get_data(file)[0][0][0] == 'ic motor'


    # return store_data, records



# if __name__ == "__main__":

    # d, r = test_1()