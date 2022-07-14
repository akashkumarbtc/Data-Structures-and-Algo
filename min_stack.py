class Node:
    def __init__(self, value = None, next = None, min = None):
        self.value = value
        self.next  = next
        self.min = min


class CustomStack:

    def __init__(self):
        self.top = None
        

    def is_empty(self):
        if self.top == None:
            return True
        return False

    def min_val(self):
        if not self.top:
            return None
        return self.top.min

    def push(self, value):
        min_val = 0
        if self.top and self.top.min < value:
            min_val = self.top.min   
        else:
            min_val = value
        new_node = Node(value, self.top, min_val)
        self.top = new_node

    def pop(self):
        if not self.top:
            return "No elements in stack"
        item = self.top.value
        self.top = self.top.next
        return item

    def print_stack(self):
        temp = self.top

        while temp:
            print(temp.value)
            temp = temp.next


stack = CustomStack()

stack.push(5)
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.min_val())

stack.push(0)
print(stack.min_val())
