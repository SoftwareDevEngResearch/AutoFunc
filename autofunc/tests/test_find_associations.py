from autofunc.find_associations import find_associations
from autofunc.get_data import get_data
import os.path


def test_1():

    script_dir = os.path.dirname(__file__)
    file1 = os.path.join(script_dir, '../assets/bladeCombined.csv')

    store_data, records = get_data(file1)

    conf_results, results = find_associations(store_data,records)

    assert conf_results['screw'][0][0] == 'couple solid'


def test_2():

    script_dir = os.path.dirname(__file__)
    file1 = os.path.join(script_dir, '../assets/bladeCombined.csv')

    store_data, records = get_data(file1)

    conf_results, results = find_associations(store_data, records)

    assert len(results['screw']) == 3