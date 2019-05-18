
"""

Use top XX% of results as a threshold for the functions and flows that are associated with each component

"""

def get_top_results(conf_results, threshold = 0.7):

   # Empty dictionary to collect top percentage of threshold
   thresh_results = {}

   # Counter to keep track of sum of confidences through the top results
   so_far = 0

   # Counter to keep track of how many function-flows were used to reach sum threshold
   i = 0

   # Sum confidence values for each CFF
   for k,v in conf_results.items():

      while so_far <= threshold:

         # Each value is a list of list, iterate through the outer list
         for vs in v:

            if so_far <= threshold:

               # Sum confidence values
               so_far += vs[1]

               # Keep track of list index for appending resulting CFF combinations
               i += 1

      # For the results dictionary, append a list of all resulting function-flows that fell within the threshold
      thresh_results.setdefault(k, []).append(v[0:i])

      # Reset index counter and confidence sum
      i = 0
      so_far = 0

   # # Test for summing confidences
   # conf_sum = 0
   # for k,v in thresh_results.items():
   #    for vs in v[0]:
   #       conf_sum += vs[1]
   #
   #    # print('{0}: {1}'.format(k,conf_sum))
   #    conf_sum = 0

   return thresh_results