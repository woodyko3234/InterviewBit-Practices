from math import factorial
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        ##To solve this problem I used a method I once saw on Quora
        ##to properly create lexical permutations.
        ##I will link to it here. Very good resource
        ##https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering
        result = []
        size = len(A)
        A.sort()
        for _ in range(factorial(size)):
            result.append(list(A))
            x = size-2
            while x>0 and A[x] > A[x+1]:
                x -= 1
            y = x+1
            while y<size and A[x] < A[y]:
                y += 1
            y-=1
            A[x], A[y] = A[y], A[x]
            A = A[:x+1] + list(reversed(A[x+1:]))
        return result
