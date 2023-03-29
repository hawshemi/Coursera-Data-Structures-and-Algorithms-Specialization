# Uses python3


def edit_distance(s, t):
    """Edit distance between two strings.

    The edit distance between two strings is the minimum number of insertions,
    deletions, and mismatches in an alignment of two strings.

    Samples:
    >>> edit_distance("ab", "ab")
    0
    >>> edit_distance("short", "ports")
    3
    >>> # Explanation: s h o r t −
    >>> #              − p o r t s
    >>> edit_distance("editing", "distance")
    5
    >>> # Explanation: e d i − t i n g −
    >>> #              − d i s t a n c e
    """
    len_s = len(s) + 1
    len_t = len(t) + 1

    # Create a distance matrix and write in initial values.
    d = [[x] + [0] * (len_t - 1) for x in range(len_s)]
    d[0] = [x for x in range(len_t)]

    for i in range(1, len_s):
        for j in range(1, len_t):

            # Levenshtein distance calculation.
            if s[i - 1] == t[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1]) + 1

    # The last element of the matrix is edit distance metric.
    return d[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))