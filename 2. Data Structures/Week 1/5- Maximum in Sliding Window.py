import sys

class FastScanner:
    def __init__(self):
        self.inpt = sys.stdin.readline().split()
        self.index = 0

    def next(self):
        if self.index >= len(self.inpt):
            self.index = 0
            self.inpt = sys.stdin.readline().split()
        res = self.inpt[self.index]
        self.index += 1
        return res

    def next_int(self):
        return int(self.next())


def solve():
    scanner = FastScanner()
    n = scanner.next_int()
    a = [0] * n
    for i in range(n):
        a[i] = scanner.next_int()
    m = scanner.next_int()
    deque = []
    for i in range(n):
        if deque and deque[0] == i - m:
            deque.pop(0)
        while deque and a[deque[-1]] < a[i]:
            deque.pop()
        deque.append(i)
        if i + 1 >= m:
            print(a[deque[0]])
    print()


if __name__ == '__main__':
    solve()
