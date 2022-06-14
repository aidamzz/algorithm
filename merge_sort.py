def merge(R, L, A, i, j, a, b):
    if a < b:
        if j<= 0 or (i>0 and L[i-1] > R[j-1]):
            A[b-1] = L[i-1]
            i -= 1
        else:
            A[b-1] = R[j-1]
            j -= 1
        merge(R,L,A,i,j,a,b-1)


def merge_sort(A, a = 0, b = None):
    if b is None: b = len(A)
    if 1 < b - a:
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:c], A[c:b]
        merge(L, R, A, len(L), len(R), a, b) 