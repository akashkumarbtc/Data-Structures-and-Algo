class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def distance_btw_lca(root, num, dist):
    if not root:
        return -1

    if root.data == num:
        return dist

    l = distance_btw_lca(root.left, num, dist+1)
    if l != -1:
        return l
    return distance_btw_lca(root.right, num, dist+1)


def find_LCA(root, n1, n2):
    if not root:
        return None

    if root.data == n1 or root.data == n2:
        return root

    l = find_LCA(root.left, n1, n2 )
    r = find_LCA(root.right, n1, n2 )

    if l and r:
        return root
    return l if l != None else r
    

def distance_btw_nodes(root, n1, n2):

    lca = find_LCA(root, n1, n2)

    dist1 = distance_btw_lca(lca, n1, 0)
    dist2 = distance_btw_lca(lca, n2, 0)

    total_distance = dist1 + dist2

    return total_distance





node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.right.right= Node(7)
node.right.left = Node(6)
node.left.right = Node(5)
node.right.left.right = Node(8)


print(distance_btw_nodes(node,4, 8))