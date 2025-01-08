# Time Complexity O(log n)
# Space Complexity O(log n)

import numpy as np

def fibonacci_matrix(n):
    if n <= 1:
        return n
    F = np.array([[1, 1], [1, 0]], dtype=object)
    result = np.linalg.matrix_power(F, n-1)
    return result[0,0]