#Euclidean Algorithm

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
