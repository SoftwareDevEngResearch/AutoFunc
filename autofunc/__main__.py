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
parser.add_argument('-lf', '--learning_file',
                    required=True,
                    type=str,
                    help='Name of the file used for data mining'
                    )

parser.add_argument('-tf', '--test_file',
                    required=True,
                    type=str,
                    help='Name of the file used for verification'
                    )

parser.add_argument('-m', '--method',
                    required=False,
                    default = 'cp',
                    type=str,
                    help='Which  method to use, association rules or conditional probabilities'
                    )

parser.add_argument('-thr', '--threshold',
                    required=False,
                    type=float,
                    default=0.7,
                    help='Threshold for top percentage of results'
                    )
parser.add_argument('-wf', '--write_file',
                    required=False,
                    default=False,
                    type=str,
                    help='File name to write to'
                    )

args = parser.parse_args(sys.argv[1:])

# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args.name))

""" Example showing how to find the match factor using the simple counting file """

# Dataset used for data mining
script_dir = os.path.dirname(__file__)
file1 = os.path.join(script_dir, args.lf)



if args.method == 'ar':
    # Convert file to data frame and list
    store_data, records = get_data(file1)

    # Use Association Rules to sort the functions/flows of components by confidence
    conf_results, results = find_associations(store_data, records)

    threshold = args.thr

    # Use a threshold to get the top XX% of confidence values
    thresh_results = get_top_results(conf_results, threshold)


else:
    comb_sort = count_stuff(file1)
    thresh_results = find_top_thresh(comb_sort, threshold)


# Use a known product for verification
test_file = os.path.join(script_dir, args.tf)

test_data, test_records = get_data(test_file)

# Find the match factor of the verification test by comparing the learned results with the known function/flows
learned_dict, matched, overmatched, unmatched, match_factor = match(thresh_results, test_records)

print('Match factor = {0:.5f}'.format(match_factor))



# Input:
# autofunc, learning_file.csv, test_file.csv, method = ar or sc, output_file_name

# if ar:
# get_data(learning_file)

# if sc:
# simple_counter(learning_file)
#
# find_top_thresh
# write_res
# get_match


# if __name__ == "__main__":

