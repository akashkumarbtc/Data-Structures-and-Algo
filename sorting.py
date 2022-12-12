a = [3,4,3,4,4,5,12,7,8]
#bubble sort
# for i in range(len(a) - 1):
#     for j in range(len(a) - i - 1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]


# quick sort 
#        i 
#i                j
#  3,4,3,4,4,5,12,7,8
def partition(arr, low, high):

    i = low
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return (i)


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


quicksort(a, 0 , len(a) - 1)
print(a)


# def merge_sort(a):
#     if len(a) == 0 or len(a) == 1: return a

#     mid = len(a) // 2
#     left_half = a[mid:]
#     right_half = a[:mid]

#     merge_sort(left_half)
#     merge_sort(right_half)

#     i,j,k = 0, 0, 0

#     while i < len(left_half) and j < len(right_half):
#         if left_half[i] < right_half[j]:
#             a[k] = left_half[i]
#             i += 1
#         else:
#             a[k] = right_half[j]
#             j += 1

#         k += 1

#     while i < len(left_half):
#         a[k] = left_half[i]
#         i += 1
#         k += 1 #
    
#     while j < len(right_half):
#         a[k] = right_half[j]
#         j += 1
#         k += 1 #

#     return a



# a  = merge_sort(a)
# print(a)

b = [1,2,3,4,5,6,7,8,9,10]

def bsearch ( a, target):
    low = 0
    high = len(a)
    mid = low + high // 2

    while low <= high and low < mid < high:
        if a[mid ] == target:
            return mid
        elif a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

        mid = (low+high)// 2

    return -1

print(bsearch(b , 11))