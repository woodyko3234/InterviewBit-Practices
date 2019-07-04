class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        to_update = 0
        show_nd = False
        for i in range(1, n):
            if A[i] == A[to_update] and show_nd == False:
                A[to_update+1] = A[i]
                show_nd = True
                to_update += 1
            elif A[i] == A[to_update] and show_nd == True: continue
            else:
                A[to_update+1] = A[i]
                to_update += 1
                show_nd = False
        A = A[:to_update+1]
        return len(A)        
