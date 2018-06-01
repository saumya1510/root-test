"""
Functions to manipulate and operate on Python in-built objects: Tuples and Dictionaries.
"""

def addValuesFromTuples(a, b):
	"""
	Adds values of two tuples of equal lengths and returns the tuple of sums.
	Args:
		a, b: two tuples of equal length > 1
	Returns:
		tuple: tuples of sum of each value of the tuple.
				Eg. for a and b as (1, 2, 3) and (2, 3, 4)
					returns: (3, 5, 7)
	"""
	if not isinstance(a, tuple) or not isinstance(b, tuple):
		print("Both the objects should be tuples of more than two values.")
		return
	if len(a) != len(b):
		print("Can't add tupples of unequal lengths")
		return 
	try:
		return tuple(map(sum, zip(a, b)))
	except Exception as e:
		print(e)
		return a


def sortDictionaryByValues(dictionary, sortingIndex = 0, reverse = False):
	"""
	Sorts a dictionary with list or tuple of values by the values. 
	Args:
		Dictionary: dictionary of the form {key : (a, b, c...)} or {key: [a, b, c..]}
		sortingIndex: index of the list by which the dictionary needs to be sorted.
		reverse: Boolean, sorts it in reverse if True.
	Returns:
		Keys: List of keys from the sorted dictionary.
	"""
	return sorted(dictionary.keys(), key = lambda x: dictionary[x][sortingIndex], reverse = reverse)
