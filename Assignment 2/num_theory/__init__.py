def num_theory(digits, width, num):
    """ Find the first 'width' digit prime in the decimal expansion of 'num'
    
    Inputs
    ------
    digits: int
        number of digit places for expansion
    width: int
        represent the first 'width' digits
    num: int or float or mathematical expression
        represent the number to be expanded
    
    Output
    ------
    int
        the first prime number
    """
    # Only keep the digits to the right of the decimal point
    n = str(pi_expansion(digits, num)).split('.')[-1]
    # Loop through all the possible windows
    for i in window(n, width):
        # Check if the window is a prime number
        if prime(int(''.join(i))):
            # Return the first prime number
            return int(''.join(i))
    return 'No Prime'