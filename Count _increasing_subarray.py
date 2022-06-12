def count_subarray(A):
    current = 1
    n = len(A)
    count = 1
    length =1 
    for i in range(1, n):
        if A[i-1] < A[i]:
            current += 1
        else:
            current = 1 
        if current == length:
            count +=1
        elif current > length:
            count = 1
            length = current
    return count
        
