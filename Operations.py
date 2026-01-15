# def addition (x, y):
#     return x + y

# def subtraction (x, y):
#     return x - y

# def multiplication (x, y):
#     return x * y

# def division (x, y):
#     return x / y

# def convert_int_float (input):
#     try:
#         return int(input)
#     except ValueError:
#         try:
#             return float(input)
#         except ValueError:
#             print("N'est pas un nombre")

# print("Choisir operation : \n1) Addition\n2) Soustraction\n3) multiplication\n4) Division ")
# choice = input("Choix : ")

# match choice:
#     case 1:
#         print(addition(convert_int_float(input()),convert_int_float(input())))
#     case 2:
#         print(subtraction(convert_int_float(input()),convert_int_float(input())))
#     case 3:
#         print(multiplication(convert_int_float(input()),convert_int_float(input())))
#     case 4:
#         print(division(convert_int_float(input()),convert_int_float(input())))


import re

def convert_int_float (input):
    try:
        return int(input)
    except ValueError:
        try:
            return float(input)
        except ValueError:
            return input

def parse_string_calculation(chain):
    parsed = re.findall(r'(?<!\d)-?\d+\.?\d*|[-+*/]', chain) #r for rawstring, d for digit, . for decimals, * numbers after the dot, then comes the symbols
    print(parsed)
    clean_list_parsed_numerically= [convert_int_float(chain) for chain in parsed]
    print(clean_list_parsed_numerically)
    return clean_list_parsed_numerically
    # for i in range(len(parsed)):
    #     print (parsed[i])

def priority_calculation(parsed_chain):
    i = 0
    while i < len(parsed_chain):
        if parsed_chain[i] in ['*', '/']:
            result = 0
            previous = parsed_chain[i-1]
            next = parsed_chain[i+1]
            
            if parsed_chain[i] == '*': result = previous * next
            elif parsed_chain[i] == '/': result = previous / next
            
            parsed_chain[i-1:i+2] = [result] # old index becomes a new one
            i -= 1 #we go back a step 
        else:
            i += 1
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

priority_calculation(parse_string_calculation(input()))


