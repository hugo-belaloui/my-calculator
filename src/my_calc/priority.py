def priority_calculation(parsed_chain):

    '''
    main function for the calculations, two loops to
    navigate through our list to do the calculations accodring to
    PEMDAS, first loop seeks for the multiplication and divison do 
    the calculation then overwrite the previous value in the index etc...
    '''
    i = 0
    
    while i < len(parsed_chain):
        if parsed_chain[i] in ['*', '/']:
            a = parsed_chain[i-1]
            b = parsed_chain[i+1]

            if parsed_chain[i] == '*':
                result = a * b
            else:
                if b == 0:
                    return "Error : cannot divide by 0"
                result = a / b

            parsed_chain[i-1:i+2] = [result]
            i -= 1
        else:
            i += 1

    i = 0
    
    while i < len(parsed_chain):
        if parsed_chain[i] in ['+', '-']:
            a = parsed_chain[i-1]
            b = parsed_chain[i+1]

            if parsed_chain[i] == '+':
                result = a + b
            else:
                result = a - b

            parsed_chain[i-1:i+2] = [result]
            i -= 1
        else:
            i += 1

    return parsed_chain[0]
