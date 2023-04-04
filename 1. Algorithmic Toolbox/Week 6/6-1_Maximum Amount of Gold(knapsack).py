# Uses python3
import sys


def optimal_weight(W, w):
    # write your code here
    matrix=[[0]*(W+1) for i in range(len(w)+1)]
    for i in range(1,len(w)+1):
        for j in range(1,W+1):
            if j>=w[i-1]:
                matrix[i][j]=max(matrix[i-1][j-w[i-1]]+w[i-1],matrix[i-1][j])
            else:
                matrix[i][j]=matrix[i-1][j]
    return matrix[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))