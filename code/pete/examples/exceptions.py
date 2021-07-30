nums = [1, 2, '3', 4]

for num in nums:
	try:
		print(num + 1)
	except TypeError:
		print(num + ' is of the wrong type ' + str(type(num)))