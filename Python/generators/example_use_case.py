#
# example_use_case.py
# An simple use of a generator to find a correct combination
# Last Modified: 8/23/2017
# Modified By: Andrew Roberts
#

CORRECT = (5, 5, 5)

def comb():
	for i in range(10):
		for j in range(10):
			for k in range(10):
				yield (i, j, k)

for (i, j, k) in comb():
	print(i, j, k)
	if (i, j, k) == CORRECT:
		break
