from autofunc.simple_counter import count_stuff
from autofunc.get_func_rep import get_func_rep
from autofunc.get_top_results import get_top_results
import os.path

def test_1():

    """ Example showing how to automate result finding with probability values  """


    # Dataset used for data mining
    script_dir = os.path.dirname(__file__)
    file1 = os.path.join(script_dir, '../assets/bladeCombined.csv')

    comb_sort = count_stuff(file1)

    # Use a threshold to get the top XX% of confidence values
    threshold = 0.5
    thresh_results = get_top_results(comb_sort, threshold)

    # Use a known product for verification
    input_file = os.path.join(script_dir, '../assets/InputExample.csv')

    # Get dictionary of functions and flows for each component based on data mining
    results, unmatched = get_func_rep(thresh_results, input_file, True)

    assert results['screw'][0][0] == 'couple solid'
    assert 'cheese' in unmatched



def test_2():

    """ Example showing how to automate result finding without probability values """


    # Dataset used for data mining
    script_dir = os.path.dirname(__file__)
    file1 = os.path.join(script_dir, '../assets/bladeCombined.csv')

    comb_sort = count_stuff(file1)

    # Use a threshold to get the top XX% of confidence values
    threshold = 0.5
    thresh_results = get_top_results(comb_sort, threshold)

    # Use a known product for verification
    input_file = os.path.join(script_dir, '../assets/InputExample.csv')

    # Get dictionary of functions and flows for each component based on data mining
    results, unmatched = get_func_rep(thresh_results, input_file, False)

    assert results['screw'][0] == 'couple solid'
    assert 'cheese' in unmatched
