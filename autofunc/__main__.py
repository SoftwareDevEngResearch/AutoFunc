from autofunc.get_match_factor import match
from autofunc.simple_counter import count_stuff, find_top_thresh
from autofunc.get_data import get_data
import os.path

import sys
import argparse

# construct the argument parse and parse the arguments
parser = argparse.ArgumentParser(
    description='This is a simple command-line program.'
    )
parser.add_argument('-n', '--name', required=True,
                    help='name of the user'
                    )
args = parser.parse_args(sys.argv[1:])

# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args.name))

""" Example showing how to find the match factor using the simple counting file """


# Dataset used for data mining
script_dir = os.path.dirname(__file__)
file1 = os.path.join(script_dir, '../assets/bladeCombined.csv')

comb_sort = count_stuff(file1)

# Use a threshold to get the top XX% of confidence values
threshold = 0.7
thresh_results = find_top_thresh(comb_sort, threshold)

# Use a known product for verification
test_file = os.path.join(script_dir, '../assets/jigsawQuery.csv')

test_data, test_records = get_data(test_file)

# Find the match factor of the verification test by comparing the learned results with the known function/flows
learned_dict, matched, overmatched, unmatched, match_factor = match(thresh_results, test_records)

print('Match factor = {0:.5f}'.format(match_factor))


if __name__ == "__main__":

