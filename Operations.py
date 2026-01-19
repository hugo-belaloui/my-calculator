import re #regex lib

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

def parse_string_calculation(chain):
    '''
    Function that takes as a parameter an equation as a string
    and using the library re(gex) parse the chain to only retrieve
    the numbers and symbols
    '''
    parsed = re.findall(r'(?<!\d)-?\d+\.?\d*|[-+*/]', chain) #r for rawstring, d for digit, . for decimals, * numbers after the dot, then comes the symbols
    clean_list_parsed_numerically= [convert_int_float(chain) for chain in parsed] #call the previous function to convert the numbers of our lists into integer and floats 
    return clean_list_parsed_numerically


def priority_calculation(parsed_chain):
    '''
    main function for the calculations, two loops to
    navigate through our list to do the calculations accodring to
    PEMDAS, first loop seeks for the multiplication and divison do 
    the calculation then overwrite the previous value in the index etc...
    '''
    i = 0
    while i < len(parsed_chain): #navigate through our list
        if parsed_chain[i] in ['*', '/']: #look for symbols
            result = 0
            previous = parsed_chain[i-1] #previous index
            next = parsed_chain[i+1] #next index
            
            if parsed_chain[i] == '*': result = previous * next #do the calculations
            elif parsed_chain[i] == '/': result = previous / next
            
            parsed_chain[i-1:i+2] = [result] #overwrite i-1 index with the result
            i -= 1 #we go back a step 
        else:
            i += 1 #we go on if no symbol found
    i = 0
    while i < len(parsed_chain):
        if parsed_chain[i] in ['+', '-']:
            result = 0
            previous = parsed_chain[i-1]
            next = parsed_chain[i+1]
            
            if parsed_chain[i] == '+': result = previous + next
            elif parsed_chain[i] == '-': result = previous - next
            
            parsed_chain[i-1:i+2] = [result]
            i -= 1
        else:
            i += 1
            
    print (parsed_chain[0])


while True:
    try:
        parsed_chain = parse_string_calculation(input("Entrez votre calcul : ")) #input the equation and parse it by calling the adequate function
        
        if not parsed_chain:
            print("Erreur : Entrée invalide. Veuillez entrer des chiffres et des symboles")
            continue 
        
        priority_calculation(parsed_chain)
        break
    except (IndexError, ValueError, TypeError): #dealing with errors
        print("Erreur : L'équation est mal formée (ex: opérateur sans chiffre)")
