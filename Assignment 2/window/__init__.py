from itertools import islice
def window(it, n):
    """ Generate sliding window of a specified width from a long iterable
    
    Inputs
    ------
    it: str
        a string of number to be iterated
    n: int
        width of the sliding window
    
    Output
    ------
    tuple
        Output sliding window based on the width specified starting from the index 0th position of the string
    """
    # Convert input to an object which can be iterate one element at a time
    iter_object = iter(it)
    # The first result is equal to the first 'n' digits of the long iterable
    result = tuple(islice(iter_object, n))
    # Output the first result
    if len(result) == n:
        yield result
    # Loop through all the elemts after the first 'n' digits
    for elem in iter_object:
        # Slide to the right and update the window result
        result = result[1:] + (elem,)
        yield result