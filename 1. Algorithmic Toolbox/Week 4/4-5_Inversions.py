def merge_and_count(left, right):
    i = j = 0
    count = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            count += len(left) - i
    result += left[i:]
    result += right[j:]
    return result, count

def count_inversions(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    left, x = count_inversions(a[:mid])
    right, y = count_inversions(a[mid:])
    merged, z = merge_and_count(left, right)
    return merged, x + y + z

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    _, count = count_inversions(elements)
    print(count)
