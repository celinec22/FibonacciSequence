import time
from fibonacci_naive import fibonacci_naive
from fibonacci_memo import fibonacci_memo

def main():
    n = 2
    start = time.time()
    print(f"Naive Recursive Fibonacci({n}): {fibonacci_naive(n)}")
    print(f"Naive Recursive Time: {time.time() - start:.5f} seconds")

    start = time.time()
    print(f"Memo Recursive Fibonacci({n}): {fibonacci_memo(n)}")
    print(f"Memo Recursive Time: {time.time() - start:.5f} seconds")

if __name__ == "__main__":
    main()