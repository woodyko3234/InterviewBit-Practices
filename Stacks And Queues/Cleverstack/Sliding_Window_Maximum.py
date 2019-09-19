import collections
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def slidingMaximum(self, nums, k):
        res = []
        d = collections.deque()
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d.append(i)
            
            if d[0] == i - k:
                d.popleft()          
            if i >= k - 1:
                res.append(nums[d[0]])
        return res 
