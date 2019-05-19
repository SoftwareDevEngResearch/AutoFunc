import itertools

def match(thresh_results, test_records):

   # store_data, records, test_list, test_case = get_data(learning_file, test_file)
   # thresh_results = find_top_conf(learning_file, test_file)


   # Make dictionary of actual CFF combinations from test case
   test_actual = {}

   # Remove duplicates from input set of test components
   k = test_records

   k.sort()
   list(k for k,_ in itertools.groupby(k))

   # Create dictionary of format: {component: [function-flow1, function-flow 2, etc.]}
   for e in k:

      # Make dictionary of list of function-flows for each component
      test_actual.setdefault(e[0], []).append(e[1])

   # List for keeping track of which function-flows happen for each component
   keep_flows = []

   # Dictionary for keeping CFF combinations from the learning set
   learned_dict = dict()

   for k,v in thresh_results.items():

      for vs in v:

         # Append list of all of the function-flows for each component
         keep_flows.append(vs[0])

      # Save list of function-flows for each component
      learned_dict[k] = keep_flows

      # Reset list for each component
      keep_flows = []


   # Empty dictionaries for each category
   overmatched = {}
   matched = {}
   unmatched = {}

   # Zeroed number for each factor to sum
   overmatched_factor = 0
   unmatched_factor = 0
   matched_factor = 0

   for k, v in test_actual.items():

      # Skip unclassified components
      if k != 'unclassified':

         # Make a set for the lists of function-flows for each component
         actual_flows = set(v)
         learned_flows = set(learned_dict[k])

         # Make dictionary for each component based on which category it falls in to

         # If component is in the learning set but not in the test case, it is overmatched
         overmatched[k] = learned_flows.difference(actual_flows)

         # If component is in the test case but not in the learning set, it is unmatched
         unmatched[k] = actual_flows.difference(learned_flows)

         # If component is in both sets, it is matched
         matched[k] = actual_flows.intersection(learned_flows)


         # Keep running sum of how many function-flows fell into each category
         overmatched_factor += len(overmatched[k])
         unmatched_factor += len(unmatched[k])
         matched_factor += len(matched[k])


   # Find overall match factor
   match_factor = matched_factor / (unmatched_factor + overmatched_factor)

   print('Match factor = {0:.5f}'.format(match_factor))


   return learned_dict, matched, overmatched, unmatched, match_factor