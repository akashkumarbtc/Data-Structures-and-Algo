def heapify(arr, n, i):
    left_cindex = i * 2 + 1
    right_cindex = i * 2 + 2

    largest = i

    if left_cindex < n and arr[largest] < arr[left_cindex]:
        largest = left_cindex

    if right_cindex < n and arr[largest] < arr[right_cindex]:
        largest = right_cindex

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)



def heap_sort(arr):
    n = len(arr)

    # create a max-heap tree.
    # heapify all the parents - parents are usually till n / 2 - 1
    for i in range(n//2 -1, -1, -1):
        heapify(arr, n, i)

    # since it is a max-heap 0th index is max element
    # swap 0th index and last index (j) and decrement j
    # heapify 0th index and repeat for all elements in arr

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i , 0)            #  consider only remaining array elements .. imp


input_arr = [3,1,2,4,3,7,2,6,7,8,10,23]

heap_sort(input_arr)

print(input_arr)