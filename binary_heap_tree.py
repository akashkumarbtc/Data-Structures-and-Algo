class BinaryHeap:
    def __init__(self):
        self.datalist = [None] * 10
        self.len = 0

    def __str__(self):
        if self.len == 0: 
            return "No elements in binary heap"
        for i in range(1, self.len+ 1):
            print(self.datalist[i])
        return ""

    def peek(self):
        if self.len == 0: 
            return "No elements in Binary Heap"
        return self.datalist[1]

    def heapify_insert(self, index):
        parent_index = int(index / 2)
        if index <= 1: 
            return
        
        if self.datalist[index] < self.datalist[parent_index]:
            self.datalist[index], self.datalist[parent_index] = self.datalist[parent_index], self.datalist[index]
        
        self.heapify_insert(parent_index)

    
    def insert(self, value):
        self.datalist[self.len + 1] = value
        self.len += 1
        self.heapify_insert(self.len)
        return "Value is inserted"


    def heapify_extract(self, index):
        left_index = (index * 2)
        right_index = (index * 2) + 1

        swapChild = 0

        if left_index > self.len:
            return
        if left_index == self.len:
            if self.datalist[left_index] < self.datalist[index]:
                self.datalist[left_index], self.datalist[index] = self.datalist[index] , self.datalist[left_index]
            return

        else:
            swapChild = left_index if self.datalist[left_index] < self.datalist[right_index] else right_index
            print("swap " + str(swapChild))

            if self.datalist[swapChild ]  < self.datalist[index]:
                self.datalist[index ], self.datalist[swapChild] = self.datalist[swapChild] , self.datalist[index ]

        self.heapify_extract(swapChild)


    def extract(self):
        if self.len == 0: 
            return
        extracted_node = self.datalist[1]
        self.datalist[1] = self.datalist[self.len]
        self.datalist[self.len] = None
        self.len -= 1
        self.heapify_extract(1)
        return extracted_node





bht = BinaryHeap()

bht.insert(5)
bht.insert(10)
bht.insert(20)
bht.insert(30)
bht.insert(40)
bht.insert(50)
bht.insert(60)
bht.insert(80)
# bht.insert(1)


# print(bht)
x = bht.extract()
print(x)
print(bht)