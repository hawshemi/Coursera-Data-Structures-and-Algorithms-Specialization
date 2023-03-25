def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    # find the Pisano period for m=10
    pisano_period = [0, 1]
    previous, current = 0, 1
    for i in range(2, 60):
        previous, current = current, (previous + current) % 10
        if previous == 0 and current == 1:
            pisano_period.pop()
            break
        else:
            pisano_period.append(current)

    # calculate the sum of the squares of the Pisano period
    pisano_period_sum_squares = sum([x*x for x in pisano_period])

    # calculate the sum of the squares of the Fibonacci sequence modulo 10
    n %= len(pisano_period)
    fibonacci_sum_squares = sum([x*x for x in pisano_period[:n+1]])

    return fibonacci_sum_squares % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
