import re
from . import convert_int_float as cif

def parse_string_calculation(chain):
    '''
    Function that takes as a parameter an equation as a string
    and using the library re(gex) parse the chain to only retrieve
    the numbers and symbols
    '''
    parsed = re.findall(r'(?<!\d)-?\d+\.?\d*|[-+*/]', chain) #r for rawstring, d for digit, . for decimals, * numbers after the dot, then comes the symbols
    clean_list_parsed_numerically= [cif.convert_int_float(chain) for chain in parsed] #call the previous function to convert the numbers of our lists into integer and floats 
    return clean_list_parsed_numerically