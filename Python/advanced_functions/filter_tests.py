#
# filter_tests.py
# Exploring the filter function 
# Last Modified: 8/16/2017
# Modified By: Andrew Roberts
#

import numpy as np

# Test 1
print("Test 1")
print("Multiples of 9: ", list(filter((lambda x: x % 9 == 0), np.random.randint(low=1,high=1000, size=100 ))))
