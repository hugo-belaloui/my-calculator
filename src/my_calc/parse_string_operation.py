import re
from . import intfloat as cif
def parse_string_calculation(chain):
    parsed = re.findall(r'(?<!\d)-?\d+\.?\d*|[-+*/]', chain)
    return [cif.convert_int_float(x) for x in parsed]