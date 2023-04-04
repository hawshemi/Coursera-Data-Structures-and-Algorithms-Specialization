from collections import deque
import sys

class StackWithMax():
    def __init__(self):
        self.stack = deque()
        self.max_stack = deque()

    def push(self, a):
        self.stack.append(a)
        if not self.max_stack or a >= self.max_stack[-1]:
            self.max_stack.append(a)

    def pop(self):
        assert len(self.stack)
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        self.stack.pop()

    def max(self):
        assert len(self.stack)
        return self.max_stack[-1]

if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert 0
