nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]


for item in (item for lst in nested_list for item in lst):
    print(item)    