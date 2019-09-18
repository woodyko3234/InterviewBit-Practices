class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        """
        Trapped: Both left and right sides are higher than it
        """
        if len(A) <= 2: return 0
        lefts, rights = [A[0]], list(A[::-1])
        leftn = rights.pop()
        curr = rights.pop()
        rightn = max(rights)
        trapped = 0
        while rights:
            if curr < leftn and curr < rightn:
                trapped += min(leftn, rightn) - curr
            #push n update
            if curr > lefts[0]:
                lefts[0] = curr
            leftn = lefts[0]
            curr = rights.pop()
            if curr == rightn and rights:
                rightn = max(rights)
        return trapped
