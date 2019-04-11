class Solution1:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        if B < A[0] or B > A[-1]: return [-1, -1]
        n = len(A)
        left_a, right_a = 0, n-1
        #find anything match first
        while left_a <= right_a:
            mid_a = (left_a + right_a) // 2
            if B == A[mid_a]:
                find_a = mid_a
                break
            elif B < A[mid_a]:
                right_a = mid_a - 1
            else:
                left_a = mid_a + 1
        try:
            find_a
        except:
            return [-1, -1]
        
        #find the boundary for B
        left_b, right_b = find_a, find_a
        left_a, right_a = 0, n-1
        while left_a <= left_b:
            find_left = (left_a + left_b) // 2
            if A[find_left] == B and left_a != find_left:
                left_b = find_left
            elif A[left_a] == B:
                find_left = left_a
                break
            else:
                left_a = find_left + 1
        while right_b <= right_a:
            find_right = (right_b + right_a+1) // 2
            if A[find_right] == B and right_a != find_right:
                right_b = find_right
            elif A[right_a] == B:
                find_right = right_a
                break
            else:
                right_a = find_right - 1
        return [find_left, find_right]
        


class Solution2:
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
