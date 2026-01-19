def convert_int_float (input):
    '''
    Function that takes as a parameter an equation as a
    string and return either an integer if one, a float if
    one or a string if it's a symbol
    '''
    try:
        return int(input) 
    except ValueError:
        try:
            return float(input)
        except ValueError:
            return input