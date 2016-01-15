def mean(vals):
    """Calculate the arithmetic mean of a list of numbers in vals"""
    assert type(vals) is list, 'wrong input format'
    total = sum(vals)
    if total == 0:
    	return 0.0
    else:
    	length = len(vals)
    	return total/length
    
#print(mean([2,4]))
#print(mean("hello"))

def test_mean():
	assert mean([2,4]) == 3.0
	
test_mean()

def test_empty_list():
	assert mean([]) == 0.0, 'emptylist'

test_empty_list()