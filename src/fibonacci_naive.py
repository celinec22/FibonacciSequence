# Time Complexity O(2^n)
# Space Complexity O(n)

def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)