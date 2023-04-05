import sys
from typing import List

swaps = []
data = []
n = 0

class Swap:
    def __init__(self, index1: int, index2: int) -> None:
        self.index1 = index1
        self.index2 = index2

def write_response() -> None:
    out.write(str(len(swaps)) + '\n')
    for swap in swaps:
        out.write(str(swap.index1) + ' ' + str(swap.index2) + '\n')

def sink(k: int) -> None:
    global n, data, swaps
    while 2 * k <= n:
        j = 2 * k
        if j < n and greater(j, j + 1):
            j += 1
        if not greater(k, j):
            break
        swap(k, j)
        k = j

def greater(i: int, j: int) -> bool:
    global data
    return data[i] > data[j]

def swap(i: int, j: int) -> None:
    global data, swaps
    temp = data[i]
    data[i] = data[j]
    data[j] = temp
    swaps.append(Swap(i - 1, j - 1))

def generate_swaps() -> None:
    global n
    for i in range(n // 2, 0, -1):
        sink(i)

def solve() -> None:
    global n, data, swaps, out
    n = int(input())
    data = [0] + list(map(int, input().split()))  # to make it 1-indexed like Java
    swaps = []
    generate_swaps()
    write_response()

if __name__ == '__main__':
    input = sys.stdin.buffer.readline
    out = sys.stdout
    solve()
    out.close()
