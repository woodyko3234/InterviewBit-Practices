class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        # For the answer to be the lexicographically smallest,
        # we want the first element to be the second smallest,
        # the 2nd element to be the smallest, and so on with
        # the rest of the sequence.
        A = sorted(A)
        for i in range(0, len(A)-1, 2):
            A[i], A[i+1] = A[i+1], A[i]
        return A
                
