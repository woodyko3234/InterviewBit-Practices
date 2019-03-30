class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        if len(A) == 0: return [-1, -1]
        
        first = self.binarySearchFirst(A, B)
        if first == -1: return [-1, -1]
        else: return [first, self.binarySearchLast(A, B)]
        
        
    def binarySearchFirst(self, A, B):
        begin = 0
        end = len(A) - 1
        
        while begin <= end:
            first = int((begin + end) / 2)
            if A[first] > B:
                end = first - 1
            elif A[first] < B:
                begin = first + 1
            else:
                end = first
                if A[begin] == B: return begin
        if A[begin] != B:
            return -1
        
    def binarySearchLast(self, A, B):
        begin = 0
        end = len(A) - 1
        
        while begin <= end:
            last = int((begin + end) / 2. + 0.5)
            if A[last] < B:
                begin = last + 1
            elif A[last] > B:
                end = last - 1
            else:
                begin = last
                if A[end] == B: return end
