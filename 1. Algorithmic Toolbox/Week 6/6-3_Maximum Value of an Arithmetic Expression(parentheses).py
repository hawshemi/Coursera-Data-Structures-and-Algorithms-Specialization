import math

def find_min(a, b, c, d, e):
    return min(a, b, c, d, e)

def find_max(a, b, c, d, e):
    return max(a, b, c, d, e)

def eval(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        assert False
        return 0

def min_max(i, j, m, M, op):
    min_val = math.inf
    max_val = -math.inf
    for k in range(i, j):
        a = eval(M[i][k], M[k+1][j], op[k])
        b = eval(M[i][k], m[k+1][j], op[k])
        c = eval(m[i][k], m[k+1][j], op[k])
        d = eval(m[i][k], M[k+1][j], op[k])
        min_val = find_min(min_val, a, b, c, d)
        max_val = find_max(max_val, a, b, c, d)
    return [min_val, max_val]

def parenthesis(exp):
    d = [int(exp[i]) for i in range(0, len(exp), 2)]
    op = [exp[i] for i in range(1, len(exp), 2)]
    m = [[0 for j in range(len(d))] for i in range(len(d))]
    M = [[0 for j in range(len(d))] for i in range(len(d))]
    for i in range(len(d)):
        m[i][i] = d[i]
        M[i][i] = d[i]
    for s in range(1, len(d)):
        for i in range(len(d)-s):
            j = i + s
            [min_val, max_val] = min_max(i, j, m, M, op)
            m[i][j] = min_val
            M[i][j] = max_val
    return M[0][len(d)-1]

exp = input()
print(parenthesis(exp))
