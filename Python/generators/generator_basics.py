#
# generator_basics.py
# Experimenting with the yield keyword in Python
# Last Modified: 8/22/2017
# Modified By: Andrew Roberts
#

def add_one(nums):
	for i in nums:
		yield(i+1)

generator_object = add_one(range(10))

# Test 1
print("\nTest 1:")
print(generator_object)
for i in generator_object:
	print(i, end=" ")
print("")

# Test 2
print("\nTest 2:")
cubes = (x**3 for x in range(5))
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))
# print(next(cubes)) Would raise StopIteration

# Test 3
print("\nTest 3:")
squares = (i*i for i in range(5))
print("Convert generator to list:", list(squares))
for x in squares:
	print(x, end=" ")
print("")
print("^Won't work after converting to list")

# Test 4
print("\nTest 4:")
added_one = add_one(range(10))
for x in added_one:
	print(x, end=" ")
print("")
print("Convert generator to list:", list(added_one))
print("^Empty because already iterated through once")

