def fibonacci_sum_optimized(n):
    if n <= 1:
        return n

    # find the remainder of n modulo 60
    n = n % 60

    # use a pre-computed lookup table to find the sum of the first k Fibonacci numbers modulo 10
    fib_sum_table = [0, 1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4, 2, 7, 0, 8, 9, 8, 8, 7, 6, 4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8, 4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0, 0]

    # return the sum of the first k Fibonacci numbers modulo 10
    return fib_sum_table[n]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_optimized(n))
