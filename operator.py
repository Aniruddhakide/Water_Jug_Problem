def rule1(j, cap_j):
    if j == cap_j:
        print("Jug is full")
    else:
        j = cap_j
    return j


def rule2(j):
    if j == 0:
        print("Jug is already empty")
    else:
        j = 0
    return j


def rule3(j1, j2, cap_j1, cap_j2):
    if j1 + j2 > cap_j1:
        n_j1 = cap_j1
        n_j2 = j2 - (cap_j1-j1)
    else:
        n_j1 = j1 + j2
        n_j2 = 0
    return n_j1, n_j2
