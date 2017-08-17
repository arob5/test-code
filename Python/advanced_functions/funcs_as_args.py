#
# funcs_as_args.py
# Exploring passing Python functions as arguments; also using Python3 annotations
# Last Modified: 8/16/2017
# Modified By: Andrew Roberts
#

def return_odd_numbers(func, num_list):
	"""Returns a list of odd numbers"""
	return [num for num in num_list if func(num)]


def is_odd(num: int) -> bool:
	"""Returns if passed in value is odd or not"""
	return num % 2 != 0

test_list = range(20)
print(return_odd_numbers(is_odd, test_list))
