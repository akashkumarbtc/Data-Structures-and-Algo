class Heap:
    def __init__(self):
        self.data  = [None] * 15
        self.len   = 0

    
    def __str__(self):
        return " - ".join(map(str, self.data))
        
    
    def insert_heapify(self, index):
        if index <= 1: return

        parent_index = index // 2
        if self.data[index] > self.data[parent_index]:
            self.data[index], self.data[parent_index] = self.data[parent_index],  self.data[index]

        self.insert_heapify(parent_index)
    
    def insert(self, value):
        self.data[self.len + 1] = value
        self.len += 1
        self.insert_heapify(self.len)

    def extract_heapify(self, index):
        left_cindex = index * 2
        right_cindex = index * 2 + 1

        if left_cindex > self.len:
            return
        if left_cindex  ==  self.len:
            self.data[index], self.data[left_cindex] = self.data[left_cindex], self.data[index]
            return

        swap_index = left_cindex if self.data[left_cindex] > self.data[right_cindex] else right_cindex
        if self.data[index] < self.data[swap_index]:
            self.data[index], self.data[swap_index]  = self.data[swap_index], self.data[index]
        self.extract_heapify(swap_index)


    def extract(self):
        self.data[1], self.data[self.len] = self.data[self.len], self.data[1]
        removed_val = self.data[self.len]
        self.data[self.len] = None
        self.len -= 1
        self.extract_heapify(1)
        return removed_val



heap = Heap()

for i in [3,1,2,4,3,7,2,6,7,8,10,23]:
    heap.insert(i)

print(heap)

print(heap.extract())
print(heap)
print("-----------------")

print(heap.extract())
print(heap)
print("-----------------")

print(heap.extract())
print(heap)
print("-----------------")
print(heap.extract())
print(heap.extract())
print(heap.extract())
print(heap.extract())