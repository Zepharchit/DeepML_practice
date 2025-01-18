import numpy as np
from collections import Counter
def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	d = Counter(y)
	sample_len = len(y)
	s = 0
	for  _,v in d.items():
		s+= (v/sample_len)**2
	
	return round(1-s,3)

y = [0, 0, 0, 0, 0, 1] 
print(gini_impurity(y))