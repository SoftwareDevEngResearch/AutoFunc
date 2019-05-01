from autofunc.simple_counter import SimpleCounter
import os.path


def test_count_stuff():

    script_dir = os.path.dirname(__file__)
    file1 = os.path.join(script_dir, '../assets/bladeCombined.csv')

    s = SimpleCounter(file1)

    assert s.count_stuff()['screw'][0][0] == 'couple solid'


def test_find_top_thresh():

    script_dir = os.path.dirname(__file__)
    file2 = os.path.join(script_dir, '../assets/bladeCombined.csv')

    s = SimpleCounter(file2)

    assert len(s.find_top_thresh(0.7)['screw']) == 1
