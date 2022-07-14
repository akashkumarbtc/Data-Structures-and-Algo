class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "Empty list"

        res = ""
        temp = self.head
        while temp:
            res += str(temp.data) + "->"
            temp = temp.next

        return res

    def insert(self, data, location):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        if location == -1:
            temp = self.head
            while temp.next:
                temp = temp.next
            
            temp.next = node
            return 

    def rearrange(self):

        prev, curr = None, self.head

        while curr:
            if curr.data < 0:
                
                node = Node(curr.data)
                node.next = self.head
                self.head = node
                if prev:
                    prev.next = curr.next
                curr = prev.next
                prev = curr

            else:
                prev = curr
                curr = curr.next
                


    def reverse_list(self):

        prev, curr = None, self.head

        while curr:
            next_node = curr.next

            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev


def reverse_list(root):

    prev, curr = None, root

    while curr:
        next_node = curr.next

        curr.next = prev
        prev = curr
        curr = next_node

    return prev



def add_linked_lists(num1, num2):
    # rev_num1 = reverse_list(num1)

    num1.reverse_list()
    carry = 0
    i = num1.head

    i.data += 1
    while i or carry:
        val1 = i.data if i else 0 
        val1 += carry
        res = val1 % 10
        carry = val1 //10
        i.data = res

        i = i.next 

    num1.reverse_list()
    print(num1)





num1 = LinkedList()
num1.insert(1,-1)
num1.insert(2,-1)
num1.insert(-3,-1)
num1.insert(4,-1)
num1.insert(-7,-1)
num1.insert(9,-1)
num1.insert(10,-1)
print(num1)


num1.rearrange()
print(num1)
# num2 = LinkedList()
# num2.insert(1,-1)


# print(add_linked_lists(num1, 1))