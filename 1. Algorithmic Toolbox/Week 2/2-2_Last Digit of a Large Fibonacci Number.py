# Use a list to store the last digits.

def fibonacci_last_digit(n):
    if n <= 1:
        return n

    last_digits = [0, 1]

    for i in range(2, n+1):
        last_digits.append((last_digits[i-1] + last_digits[i-2]) % 10)

    return last_digits[-1]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
