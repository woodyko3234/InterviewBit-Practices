class Heapsort:
    def heapsort(self, lst):
        self.build_max_heap(lst)
        for i in range(len(lst) - 1, 0, -1):
            #swap out the max heap
            lst[0], lst[i] = lst[i], lst[0]
            self.max_heapify(lst, index=0, size=i)
        return lst
        
    def parent(self,i):
        "get the parent node of i"
        return (i - 1)//2
        
    def left(self, i):
        "get the left child node of i"
        return 2*i + 1
        
    def right(self,i):
        "get the right child node of i"
        return 2*i + 2
        
    def build_max_heap(self,lst):
        length = len(lst)
        start = self.parent(length - 1)
        while start >= 0:
            self.max_heapify(lst, index=start, size=length)
            start = start - 1
        
    def max_heapify(self, lst, index, size):
        left_child = self.left(index)
        right_child = self.right(index)
        if left_child < size:
            # if there's no left_child
            # there would be no right_child as well
            # also, no child means no comparision and swap needed
            if right_child < size and lst[left_child] < lst[right_child]:
                largest = right_child
            else:
                largest = left_child
            if (lst[largest] < lst[index]):
                largest = index
            if (largest != index):
                lst[largest], lst[index] = lst[index], lst[largest]
                self.max_heapify(lst, largest, size)
