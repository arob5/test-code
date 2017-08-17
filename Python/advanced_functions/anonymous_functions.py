#
# anonymous_functions.py
# Exploring lambda functions 
# Last Modified: 8/16/2017
# Modified By: Andrew Roberts
#

import random

# Test 1
print("Test 1:")
is_even = lambda num: True if num % 2 == 0 else False
test_list = range(20)
print("Test list: ", list(test_list))
print("Evens: ", [x for x in test_list if is_even(x)])

# Test 2
print("\nTest 2:")
add_n_list = [lambda x: x+1, lambda x: x+2, lambda x: x+3]
print([func(2) for func in add_n_list])

# Test 3
h_or_t = lambda: random.choice(["H", "T"])
flip_sequence = [h_or_t() for i in range(20)]
print("Random coin flips: ", flip_sequence)
print("Num Heads: ", flip_sequence.count("H"))
print("Num Tails: ", flip_sequence.count("T"))

