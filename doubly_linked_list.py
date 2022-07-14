class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head == None:
            return "No elements in doubly linked list"
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        return ""

    def insert(self, value, location):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        
        if location == 0: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        elif location == -1:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        else:
            temp = self.head
            index = 0
            while index < location - 1:
                temp = temp.next
                index += 1

            next_node = temp.next

            temp.next = new_node
            new_node.prev = temp
            next_node.prev = new_node
            new_node.next = next_node


        
def add_list_elements(var1, var2):
    res = DoublyLinkedList()
    carry = 0

    i, j = var1.tail, var2.tail
    while i or j or carry:
        val1 = i.data if i else 0
        val2 = j.data if j else 0

        sum_val = val1 + val2 + carry
        result = sum_val % 10
        carry = sum_val // 10

        res.insert(result, 0)

        i = i.prev if i else None
        j = j.prev if j else None

    return res
    
var1 = DoublyLinkedList()
var1.insert(1,-1)
var1.insert(9,-1)
var1.insert(9,-1)
var1.insert(9,-1)
print(var1)
# 1999
var2 = DoublyLinkedList()
var2.insert(1,-1)
var2.insert(1,-1)
#11
print(var2)

print(add_list_elements(var1, var2))


