def prime(num):
    """A function that has a integer, 'num', as input and return 'True' if the number is a prime and 'False' otherwise."""
    if num > 1:
        # Loop through all the values between 2 and square root of the number 
        for i in range(2, int(num ** 0.5) + 1):
            # Check if the number is divisible (if it is divisible then it is not a prime number)
            if (num % i) == 0:
                return False
        else:
            # If the number is not divisble at all, the number is a prime number
            return True
    return False