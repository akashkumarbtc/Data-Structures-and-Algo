# def longest_peak(arr):

#     res = 0
#     for index in range(1, len(arr) - 1):
#         if arr[index - 1] < arr[index] > arr[index + 1]:

#             left = right = index 
#             while left > 0 and arr[left -1 ] < arr[left]:
#                 left -= 1
            
#             while right + 1 < len(arr) and arr[right] > arr[right + 1]:
#                 right += 1

#             res =  max( res, right - left + 1)

    
#     return res

# arr = [3, 1, 4, 1, 5, 9, 2, 6]



# print(longest_peak(arr))



"""

 Find the shortest distance between any 2 nodes in a given binary tree. 
               1 
            /      \ 
          2         3 
      /  \       /   \ 
      4    5     6   7 
    /  \                \ 
    8   9              10 
                    /    \ 
                    11  12 
                         / 
                        13 
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None




def find_lca(root, n1, n2):
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root

    left = find_lca(root.left, n1, n2)
    right = find_lca(root.right, n1, n2)

    if left and root:
        return root

    return left if left is not None else right


def calculate_distance(root, num, dist):
    if root is None:
        return -1

    if root.data == num:
        return dist

    left = calculate_distance(root.left, num, dist +1)
    if left!= -1:
        return left
    return calculate_distance(root.right, num, dist +1)



def find_shortest_distance(root, num1, num2):
    lca = find_lca(root, num1, num2)

    dist1 = calculate_distance(lca, num1, 0)
    dist2 = calculate_distance(lca, num2, 0)
    return dist1 + dist2


root = Node (1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.left.left.left = Node(8)
root.left.left.right = Node(9)

root.right.left = Node(6)
root.right.right = Node(7)

root.right.right.right = Node(10)

root.right.right.right.left = Node(11)
root.right.right.right.right = Node(12)

root.right.right.right.right.left = Node(13)


res = find_shortest_distance(root, 8, 10)
print(res)