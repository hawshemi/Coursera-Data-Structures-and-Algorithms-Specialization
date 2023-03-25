# Using Iteration

def fibonacci_number(n):
    if n <= 1:
        return n

    fib_prev = 0
    fib_current = 1

    for i in range(2, n+1):
        fib_next = fib_prev + fib_current
        fib_prev = fib_current
        fib_current = fib_next

    return fib_current


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
