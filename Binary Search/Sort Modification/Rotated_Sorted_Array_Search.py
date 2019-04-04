class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        l = len(A) #O(1)
        left = 0
        right = l - 1
        while left < right:
            pivot_in = False
            if A[left] >= A[right]:
                pivot_in = True
            mid = (left+right)//2
            if pivot_in:
                if B > A[mid]:
                    if A[right] > A[mid] and B > A[right]:
                        right = mid
                    else:
                        left = mid + 1
                elif B < A[mid]:
                    if A[left] < A[mid] and B < A[left]:
                        left = mid+1
                    else:
                        right = mid
                else: return mid
            else:
                if B > A[right] or B < A[left]: break
                if B > A[mid]:
                    left = mid+1
                elif B < A[mid]:
                    right = mid
                else:
                    return mid
        return -1
