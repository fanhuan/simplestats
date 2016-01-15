from stats import mean
from nose.tools import assert_equal, assert_almost_equals

def test_mean():
	assert_equal(mean([2,4]),3.0)
#test_mean()

def test_empty_list():
	assert_equal(mean([]), 0.0)
#test_empty_list()

def test_float():
	assert_almost_equals(mean([.5,1,.5]), 0.6666666666, 2) 
	# the last argument is the decimal places to check
#test_float()

def test_str_list_mean():
	assert_equal(mean(['1','2','3']),2.0)