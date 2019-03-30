class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        if len(A) == 0: return 0
        else:
            left, right = self.binarySearch(A,B)
            if left == right:
                return left
            else: return right


    def binarySearch(self, A, B):
        begin = 0
        end = len(A) - 1
        if A[begin] == B: return [begin, begin]
        elif A[end] == B: return [end, end]
        elif A[end] < B: return [end+1, end+1]
        elif A[begin] > B: return [0, 0]
        while begin <= end:
            mid = int((begin + end) / 2)
            if A[mid] > B:
                end = mid
            elif A[mid] < B:
                begin = mid
            else:
                return [mid, mid]

            if begin == mid and end - begin == 1:
                return [begin, end]
