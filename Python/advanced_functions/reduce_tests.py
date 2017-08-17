#
# reduce_tests.py
# Exploring the reduce function 
# Last Modified: 8/16/2017
# Modified By: Andrew Roberts
#

from functools import reduce

test_list = [.05, .2, .1, .1, .4, .1, .05]
print("Original list:", test_list)
print("Probability of sample space: ", reduce(lambda x, y: x+y, test_list))
print("Cumulative probability: ", [reduce(lambda x, y: x+y, test_list[:i]) for i in range(1, len(test_list)+1)])
