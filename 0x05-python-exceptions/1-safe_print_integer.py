#!/usr/bin/python3
def safe_print_integer(value):
    """print an integer with "{:d}".format().
    args:
    value (int):The integer to print.
    returns:
    if a TypeError or ValueError occurs - False.
    otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
