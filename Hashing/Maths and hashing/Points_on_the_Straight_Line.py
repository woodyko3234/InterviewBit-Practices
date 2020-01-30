from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        """
        on the same line => got the same slope
        y = ax + b, so points on the same line means
        they need to have the same slope(a) and same interval(b)
        """
        n = len(A)
        output = 0
        if n <= 2: return n
        for i in range(n-1):
            slopeDict = defaultdict(int)
            dup = 0
            for j in range(n):
                if A[i] == A[j] and B[i] == B[j]:
                    dup += 1
                    continue
                elif A[i] == A[j]:
                    slope = float("inf")
                elif B[i] == B[j]:
                    slope = 0
                else:
                    slope = (float(B[i] - B[j])/float(A[i] - A[j]))
                slopeDict[slope] += 1
            if slopeDict:
                temp = max(slopeDict.values())
            else: temp = 0
            temp += dup
            if temp > output:
                output = temp
        return output
