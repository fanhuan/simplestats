def mean(vals):
    """Calculate the arithmetic mean of a list of numbers in vals"""
    total = sum(vals)
    length = len(vals)
    return total/length
    
print(mean([2,4]))