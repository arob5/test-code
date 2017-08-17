#
# dynamically_declared_functions.py
# Exploring functions defined inside other functions
# Last Modified: 8/16/2017
# Modified By: Andrew Roberts
#

def return_func_append_to_string(base_string):
	"""Returns function that will append args to a base string""" 
	def concat_to(add_on):
		return base_string + str(add_on)

	return concat_to

format_dollar = return_func_append_to_string("$")

for i in range(10):
	print(format_dollar(i))
