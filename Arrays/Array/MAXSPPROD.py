class Solution:
    def _first_greater(self, A, prev=True):
        stack, ans = list(), [0] * len(A)

        it = range(len(A)) if prev else range(len(A)-1, -1, -1)

        for i in it:
            while stack and A[i] >= A[stack[-1]]:
                stack.pop()
            ans[i] = stack[-1] if stack else 0
            stack.append(i)
        return ans

    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        left = self._first_greater(A)
        right = self._first_greater(A, prev=False)
        maxx = -float('inf')

        for l, r in zip(left, right):
            maxx = max(l * r, maxx)

        return maxx % 1000000007
