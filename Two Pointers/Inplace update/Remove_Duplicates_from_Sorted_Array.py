class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        #A = list(set(A))
        #return len(A)
        #InterviewBit doesn't accept this solution lol
    
        to_update = 0
        n = len(A)
        if n <= 1: return n
        else:
            for i in range(1, n):
                if A[to_update] == A[i]: continue
                else:
                    to_update += 1
                    A[to_update] = A[i]
        A = A[:to_update+1]
        return len(A)
