from autofunc.get_match_factor import match
from autofunc.simple_counter_opt import count_stuff, find_top_thresh
from autofunc.get_data import get_data
import pandas as pd
import os.path


# Dataset used for data mining
script_dir = os.path.dirname(__file__)
file1 = os.path.join(script_dir, '../assets/bladeCombined_id.csv')

store_data = pd.read_csv(file1)

# ids = list(store_data.id.unique())
ids = list(map(int,store_data.id.unique()))


ts = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]


e = ids[0]

comb_sort, test_comb_sort = count_stuff(file1, e)
    #
    # for t in ts:
    #
    #     thresh_results = find_top_thresh(comb_sort, threshold)









# comb_sort = count_stuff(file1)
#
# # Use a threshold to get the top XX% of confidence values
# threshold = 0.7
# thresh_results = find_top_thresh(comb_sort, threshold)
#
# # Use a known product for verification
# test_file = os.path.join(script_dir, '../assets/jigsawQuery.csv')
#
# test_data, test_records = get_data(test_file)
#
# # Find the match factor of the verification test by comparing the learned results with the known function/flows
# learned_dict, matched, overmatched, unmatched, match_factor = match(thresh_results, test_records)
#
# print('Match factor