def direct_access_sort(A):
    u = 1 + max([A.index(x) for x in A])
    print(u)
    D = [None] * u
    for x in A:
        D[A.index(x)] = x
    i = 0
    for key in range(u):
        if D[key] is not None:
            print(D[key])
            A[i] = D[key]
            i += 1