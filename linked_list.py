class Node:
    def __init__(self, value = None):
        self.value = value
        self.next  = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value, location):
        currNode = Node(value)
        if self.head == None:
            self.head = currNode
            self.tail = currNode

        else: 
            if location == 0:
                currNode.next = self.head
                self.head = currNode
            elif location == -1:
                self.tail.next = currNode
                self.tail = currNode
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1

                next_node = temp.next

                temp.next = currNode
                currNode.next = next_node

    def print_ll(self):
        if self.head == None:
            print("Linked List is empty")

        else:
            temp = self.head
            while temp != None:
                print(temp.value)
                temp = temp.next


ll = LinkedList()
ll.insert(0,0)
ll.insert(1,-1)
ll.insert(2,-1)
ll.insert(3,-1)
ll.insert(4,-1)
ll.insert(5, 2)

ll.print_ll()



