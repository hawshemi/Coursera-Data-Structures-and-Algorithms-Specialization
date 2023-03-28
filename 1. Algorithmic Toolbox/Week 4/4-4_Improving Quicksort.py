from random import randint


def partition3(array, left, right):
    x = array[left]
    j, k = left, left
    for i in range(left + 1, right + 1):
        if array[i] < x:
            k += 1
            j += 1
            array[i], array[k] = array[k], array[i]
            array[j], array[k] = array[k], array[j]
        elif array[i] == x:
            k += 1
            array[i], array[k] = array[k], array[i]
    array[left], array[j] = array[j], array[left]
    return j, k


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
