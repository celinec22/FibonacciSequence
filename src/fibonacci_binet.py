# Time Complexity O(1)
# Space Complexity O(1)

import math

def fibonacci_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (-phi)**(-n)) / math.sqrt(5))
