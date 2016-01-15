import re

def mean(vals):
    """Calculate the arithmetic mean of a list of numbers in vals"""
    assert type(vals) is list, 'wrong input format'
    vals = [float(x) for x in vals]
    for item in vals:
    	if re.match('^[0-9]*',item):???
    		item = float(item)
    	assert float(item)
    total = sum(vals)
    if total == 0:
    	return 0.0
    else:
    	length = len(vals)
    	return total/length
    
#print(mean([2,4]))
#print(mean("hello"))

#unit test: test functions
def test_mean():
	assert mean([2,4]) == 3.0
test_mean()

def test_empty_list():
	assert mean([]) == 0.0
test_empty_list()