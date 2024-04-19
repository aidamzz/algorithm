def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quickSort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quickSort(array, pivot+1, high)
        quickSort(array, low, pivot-1)