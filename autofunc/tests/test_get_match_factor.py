from autofunc.get_match_factor import match
from autofunc.get_top_results import get_top_results
from autofunc.find_associations import find_associations
from autofunc.get_data import get_data
import os.path
import numpy as np


def test_1():

    """
    Tests that the match factor for a known learning set and test case is close to the known value

    """

    script_dir = os.path.dirname(__file__)
    file1 = os.path.join(script_dir, '../assets/bladeCombined.csv')

    store_data, records = get_data(file1)

    conf_results, results = find_associations(store_data, records)

    thresh_results = get_top_results(conf_results, 0.7)


    test_file = os.path.join(script_dir, '../assets/jigsawQuery.csv')

    test_data, test_records = get_data(test_file)

    learned_dict, matched, overmatched, unmatched, match_factor = match(thresh_results, test_records)

    assert np.allclose(0.82051, match_factor)
