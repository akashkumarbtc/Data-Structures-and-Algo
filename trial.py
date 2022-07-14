class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head == None:
            return  "No elements in the linked list"
        temp = self.head
        res_str = ""
        while temp:
            res_str += str(temp.data) + " -> "
            temp = temp.next

        return res_str

    def insert(self, value, location):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        
        if location == 0: 
            new_node.next = self.head
            self.head = new_node
        elif location == -1:
            self.tail.next = new_node
            self.tail = new_node
        else:
            index = 0
            temp = self.head
            while index < location - 1 and temp:
                temp = temp.next
                index += 1
            
            if temp:
                next_node = temp.next
                temp.next = new_node
                new_node.next = next_node
            else:
                print("Index out of range")

        return

        



ll = LinkedList()
ll.insert(0,0)
ll.insert(1,-1)
ll.insert(2,-1)
ll.insert(3,-1)
ll.insert(4,-1)
ll.insert(5,-1)
ll.insert(10,10)

print(ll)

