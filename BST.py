class BST:
    def __init__(self, value = None):
        self.value = value
        self.leftChild = None
        self.rightChild = None


def insert( value, root ):
    if root.value == None:
        root.value = value
    elif value <= root.value:
        if root.leftChild is None:
            root.leftChild = BST(value)
        else:
            insert(value, root.leftChild)
    else:
        if root.rightChild is None:
            root.rightChild = BST(value)
        else:
            insert(value, root.rightChild)


def preorder_traversal(root):
    if not root:
        return
    print(root.value)
    preorder_traversal(root.leftChild)
    preorder_traversal(root.rightChild)


def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.leftChild)
    print(root.value)
    inorder_traversal(root.rightChild)


def search(value, root):
    if root.value == value:
        print ("value found")

    elif value < root.value:
        if root.leftChild.value == value:
            print ("value found")
        else:
            search(value, root.leftChild)

    else:
        if root.rightChild.value == value:
            print ("value found")
        else:
            search(value, root.rightChild)


def level_order_traversal(rootNode):
    if not rootNode:
        return
    queue = []
    queue.append(rootNode)

    while  len(queue):
        root = queue.pop(0)
        print(root.value)
        if root.leftChild is not None:
            queue.append(root.leftChild)
        if root.rightChild is not None:
            queue.append(root.rightChild)


bst = BST()
insert(70, bst)
insert(50 , bst)
insert(90, bst)
insert(30, bst)
insert(60, bst)
insert(80, bst)
insert(100, bst)
insert(20, bst)
insert(40, bst)
# print(search(40, bst))
# inorder_traversal(bst)
level_order_traversal(bst)