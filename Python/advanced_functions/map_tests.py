#
# map_tests.py
# Exploring the map function 
# Last Modified: 8/16/2017
# Modified By: Andrew Roberts
#

# Test 1
print("Test 1")
print("Is even", list(map(lambda n: n%2==0, range(20))))

# Test 2
print("\nTest 2")
print("Squares: ", list(map(lambda x, y: x*y, range(10), range(10))))
