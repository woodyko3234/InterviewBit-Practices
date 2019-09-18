class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        """
        Trapped: Both left and right sides are higher than it
        """
        if len(A) <= 2: return 0
        lefts, rights = [], list(A[::-1])
        leftn = rights.pop()
        curr = rights.pop()
        rightn = max(rights)
        trapped = 0
        while rights:
            lefts = self.checkSide(lefts, leftn)
            leftn = lefts[0]
            if curr < leftn and curr < rightn:
                trapped += min(leftn, rightn) - curr
            leftn = curr
            curr = rights.pop()
            if curr == rightn and rights:
                rightn = max(rights)
        return trapped
    def checkSide(self, l, node):
        while l:
            if node >= l[-1]:
                l.pop()
            else: break
        if l == []: l.append(node)
        return l
