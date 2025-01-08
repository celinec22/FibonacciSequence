import time
from fibonacci_naive import fibonacci_naive
from fibonacci_memo import fibonacci_memo
from fibonacci_bottom_up import fibonacci_bottom_up
from fibonacci_optimized import fibonacci_optimized
from fibonacci_matrix import fibonacci_matrix
from fibonacci_binet import fibonacci_binet

def main():
    n = int(input("Enter the position (n) in the Fibonacci sequence you want to compute: "))

    start = time.time()
    print(f"Naive Recursive Fibonacci({n}): {fibonacci_naive(n)}")
    print(f"Naive Recursive Time: {time.time() - start:.5f} seconds")

    start = time.time()
    print(f"Memoized Fibonacci({n}): {fibonacci_memo(n)}")
    print(f"Memoized Time: {time.time() - start:.5f} seconds")

    start = time.time()
    print(f"Bottom-Up Fibonacci({n}): {fibonacci_bottom_up(n)}")
    print(f"Bottom-Up Time: {time.time() - start:.5f} seconds")

    start = time.time()
    print(f"Optimized Fibonacci({n}): {fibonacci_optimized(n)}")
    print(f"Optimized Time: {time.time() - start:.5f} seconds")

    start = time.time()
    print(f"Matrix Fibonacci({n}): {fibonacci_matrix(n)}")
    print(f"Matrix Time: {time.time() - start:.5f} seconds")

    start = time.time()
    print(f"Binet's Formula Fibonacci({n}): {fibonacci_binet(n)}")
    print(f"Binet's Formula: {time.time() - start:.5f} seconds")




if __name__ == "__main__":
    main()