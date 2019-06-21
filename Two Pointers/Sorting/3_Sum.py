class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        if len(A) < 3: return None
        elif len(A) == 3: return sum(A)
        sortA, n = sorted(A), len(A)
        closest = float("inf")
        for second in range(1, n-1):
            first, last = 0, n - 1
            curDiff = B - sortA[second]
            while first < second and last > second:
                if abs(sum([sortA[first], sortA[second], sortA[last]]) - B) < abs(closest - B):
                    closest = sum([sortA[first], sortA[second], sortA[last]])
                if sortA[first]+sortA[last] < curDiff:
                    first += 1
                elif sortA[first]+sortA[last] > curDiff:
                    last -= 1
                else: return closest
        return closest
