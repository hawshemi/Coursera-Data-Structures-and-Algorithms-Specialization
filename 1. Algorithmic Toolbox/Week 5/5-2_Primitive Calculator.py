# Uses python3
import sys


def optimal_sequence(n):
    """Optimal sequence from 1 to n.
    You are given a primitive calculator that can perform the following three
    operations with the current number x:
    * multiply x by 2
    * multiply x by 3
    * add 1 to x
    Your goal is given a positive integer n, find the minimum number of
    operations needed to obtain the number n starting from the number 1.
    Samples:
    >>> list(optimal_sequence(1))
    [1]
    >>> list(optimal_sequence(145))
    [1, 3, 9, 18, 36, 72, 144, 145]
    >>> list(optimal_sequence(14512))
    [1, 3, 9, 10, 11, 33, 66, 67, 201, 402, 403, 1209, 3627, 3628, 7256, 14512]
    """
    # Create a list which stores the hop count from an element to 1.
    hop_count = [0] * (n + 1)

    # Path from 1 to 1 is 1.
    hop_count[1] = 1
    for i in range(2, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i // 2)
        if i % 3 == 0:
            indices.append(i // 3)

        # Get the index with the least hop count to 1.
        min_hops = min([hop_count[x] for x in indices])

        # Write hop count from current index to 1. Hop count incremented by 1.
        hop_count[i] = min_hops + 1

    # ptr points to current position of hop_count.
    ptr = n
    optimal_seq = [ptr]
    while ptr != 1:

        # The list contains next hop candidates.
        candidates = [ptr - 1]
        if ptr % 2 == 0:
            candidates.append(ptr // 2)
        if ptr % 3 == 0:
            candidates.append(ptr // 3)

        # Choose from the candidates whose hop count is the least.
        ptr = min(
            [(c, hop_count[c]) for c in candidates],
            key=lambda x: x[1]
        )[0]
        optimal_seq.append(ptr)

    return reversed(optimal_seq)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=" ")