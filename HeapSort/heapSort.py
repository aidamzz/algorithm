def heapify(arr, n, i):
    # find largest among root and children
    largest = i
    l = 2*i +1
    r = 2*i + 2
    if l< n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[i] < arr[r]:
        largest = r
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)
        print(arr)

def heapSort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0,-1):
        #swap
        arr[i], arr[0] = arr[0], arr[1]
        heapify(arr, i , 0)