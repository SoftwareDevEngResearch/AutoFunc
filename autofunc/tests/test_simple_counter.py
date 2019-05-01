from autofunc.simple_counter import SimpleCounter
import os.path


def test_1():

    script_dir = os.path.dirname(__file__)
    file1 = os.path.join(script_dir, '../assets/bladeCombined.csv')

    s = SimpleCounter(file1)

    # s.count_stuff()

    assert s.count_stuff()['screw'][0][0] == 'couple solid'
