class Solution:
    # @param S : list of integers
    # @param target : integer
    # @return an integer
    def threeSumClosest(self, S, target):
        n = len(S)
        if n < 3: return None #no valid answer
        elif n == 3: return sum(S) #no option
        S.sort()
        first = 0
        last = n-1
        minDiff = float('inf')
        while first < (last-1):
            for i in range(first+1, last):
                newSum = S[first] + S[i] + S[last]
                if newSum == target: return target
                elif abs(newSum - target) < abs(newDiff < minDiff:
                    minDiff = newDiff
                    bestNow = newSum
            cur_sum = S[first] + S[first + 1] + S[last]
            if cur_sum > target:
                last -= 1
            else:
                first += 1
        return bestNow
