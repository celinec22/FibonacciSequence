# Time Complexity O(n)
# Space Complexity O(n)

def fibonacci_bottom_up(n) :
    if n <= 1:
        return n
    fib = [0] * (n+1)
    fib[1]= 1
    for i in range(2,n+1):
        fib[i]=fib[i-1]+fib[i-2]
    return fib[n]