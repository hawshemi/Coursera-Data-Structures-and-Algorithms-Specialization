
def get_change(m):

    total_ten = m // 10
    m %= 10
    total_five = m // 5
    m %= 5
    return total_ten + total_five + m


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))