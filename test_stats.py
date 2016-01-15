from stats import mean

def test_mean():
	assert mean([2,4]) == 3.0
test_mean()

def test_empty_list():
	assert mean([]) == 0.0
test_empty_list()

def test_float():
	assert mean([1.1,2,0.5]) == 1.2
test_float()