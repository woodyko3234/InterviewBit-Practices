class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        '''
        find a, b, c in A, B, C (sorted arrays), respectively
        that a,b,c must be as close as possible
        i.e. max(abs(A[a] - B[b]), abs(B[b] - C[c]), abs(C[c] - A[a]))
        '''
        #http://www.geeksforgeeks.org/find-three-closest-elements-from-given-three-sorted-arrays/
        p = len(A)
        q = len(B)
        r = len(C)
        min_diff = float('inf')
    
        #set beginning indexes for A, B, and C
        i = 0
        j = 0
        k = 0
        while i < p and j < q and k < r:
            minimum = min(A[i], min(B[j], C[k]))
            maximum = max(A[i], max(B[j], C[k]))
            #no need apply abs
            if (maximum - minimum) < min_diff:
                res_i = i 
                res_j = j
                res_k = k
                min_diff = maximum - minimum
            if min_diff == 0: return min_diff
            if minimum == A[i]:
                i += 1
            elif minimum == B[j]:
                j += 1
            else: k += 1
        return min_diff
