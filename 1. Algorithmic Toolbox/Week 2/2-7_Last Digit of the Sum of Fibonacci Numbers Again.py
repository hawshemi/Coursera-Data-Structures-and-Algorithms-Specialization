import sys

def fibonacci_partial_sum_memoized(from_, to, memo={0: 0, 1: 1}):
    _sum = 0
    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        if i not in memo:
            memo[i] = memo[i-1] + memo[i-2]
        current, _next = _next, memo[i]

    return _sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_memoized(from_, to))
