import time
from fibonacci_naive import fibonacci_naive
from fibonacci_memo import fibonacci_memo
from fibonacci_bottom_up import fibonacci_bottom_up

def main():
    n = 35
    start = time.time()
    print(f"Naive Recursive Fibonacci({n}): {fibonacci_naive(n)}")
    print(f"Naive Recursive Time: {time.time() - start:.5f} seconds")

    start = time.time()
    print(f"Memoized Fibonacci({n}): {fibonacci_memo(n)}")
    print(f"Memoized Time: {time.time() - start:.5f} seconds")

    start = time.time()
    print(f"Bottom-Up Fibonacci({n}): {fibonacci_bottom_up(n)}")
    print(f"Bottom-Up Time: {time.time() - start:.5f} seconds")

if __name__ == "__main__":
    main()