class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        #brute force O(n)
        #try:
        #    return list(A).index(B)
        #except:
        #    return -1
        begin = 0
        end = len(A) - 1
        
        if end == -1: return end
        
        while begin <= end:
            mid = int((begin + end) / 2)
            if B > A[mid]:
                if A[mid] > A[begin]: 
                    #same secting: increasing
                    begin = mid + 1
                else: #A[mid] < A[end]
                    if B > A[end]:
                        #A[begin] > B > A[end]
                        return -1
                    elif B < A[end]:
                        begin = mid + 1
                    else:
                        return end
            elif B < A[mid]:
                if A[mid] < A[end]: 
                    #same secting: decreasing
                    end = mid - 1
                else: #A[mid] > A[begin]
                    if B < A[end]:
                        begin = mid + 1
                    elif B > A[end]:
                        end = mid - 1
                    else:
                        return end
            else: return mid
        return -1
