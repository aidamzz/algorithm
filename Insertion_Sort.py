def insert_last(A,i):
    if i > 0 and A[i]< A[i-1]:
        A[i], A[i-1] = A[i-1], A[i]
        insert_last(A,i-1)

def insertion_sort(A, i = None):
    if i == None : i = len(A)-1
    if i >0:
        insertion_sort(A, i-1)
        insert_last(A,i)


