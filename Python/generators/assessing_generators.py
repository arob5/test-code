#
# assessing_generators.py
# Assessing time and memory usage of generators vs lists
# Last Modified: 8/23/2017
# Modified By: Andrew Roberts
#

import numpy as np
import memory_profiler as mem_profile
import time


print("Memory at start: {}".format(mem_profile.memory_usage()))

def number_list(n_elems):
	output = []
	for i in range(n_elems):
		elem = {"var1": np.random.randint(0, 10), 
			"var2": np.random.randint(0, 100), 
			"var3": np.random.randint(0, 1000)
			}	
		output.append(elem)

	return output

def number_generator(n_elems):
	for i in range(n_elems):
		elem = {"var1": np.random.randint(0, 10), 
			"var2": np.random.randint(0, 100), 
			"var3": np.random.randint(0, 1000)
			}	
		yield elem

t0 = time.clock()
#x = number_list(1000000)
x = number_generator(1000000)
t1 = time.clock()

print("Memory at end: {}".format(mem_profile.memory_usage()))
print("Time taken: {}".format(t1-t0))
