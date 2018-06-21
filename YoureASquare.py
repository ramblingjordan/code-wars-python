import math


def is_square(n): 
    return float(math.sqrt(n)).is_integer()
    

print(is_square(3))