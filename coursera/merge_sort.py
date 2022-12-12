
def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m
    
	# create temp arrays
	L = arr[l: l+n1]
	R = arr[m+1: m+1+n2]

	# Merge the temp arrays back into arr[l..r]
	i,j,k = 0, 0, l

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
        


def sort_implementation(i_array, low, high):
    if high <= low: return 
    mid = (low + high) // 2
    sort_implementation(i_array, low, mid)
    sort_implementation(i_array, mid+ 1, high)
    if i_array[mid] < i_array[mid + 1]: return #improvment 
    merge(i_array, low, mid , high)


#bottom up merge sort implementation - no recursion 


# def sort_implementation(i_array, low, high):
#     n = len(i_array)
#     i = 1
#     for i in range(1, n, i):
#         print(i)
#         for j in range (0, n-i, i+i):
#             merge(i_array, j, j + i - 1, min(j+i+i-1, n-1))

def sort():
    i_array = [5, 6, 3, 7, 2, 6, 8, 4, 7, 3]
    sort_implementation(i_array, 0, len(i_array) -1)
    print(i_array)

sort()