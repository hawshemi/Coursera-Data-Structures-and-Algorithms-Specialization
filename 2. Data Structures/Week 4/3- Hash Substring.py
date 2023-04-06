import sys

def read_input():
    return (sys.stdin.readline().rstrip(), sys.stdin.readline().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return (i for i in range(len(text) - len(pattern) + 1) if text[i:i + len(pattern)] == pattern)

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
