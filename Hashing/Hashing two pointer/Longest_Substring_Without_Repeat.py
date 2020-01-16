from collections import defaultdict
class Solution:
	# @param A : string
	# @return an integer
    def lengthOfLongestSubstring(self, A):
        longestSubL, idxFollowup = 0, defaultdict(str)
        n, recordedIdx, tempL = len(A), 0, 0
        if n <= 1: return n
        for i in range(1,n+1):
            if idxFollowup[A[i-1]] == "": pass
            elif recordedIdx <= idxFollowup[A[i-1]]:
                recordedIdx = idxFollowup[A[i-1]]
            tempL = i - recordedIdx
            #update string idx
            idxFollowup[A[i-1]] = i
            if longestSubL < tempL:
                #print(idxFollowup[A[i]], recordedIdx, tempL)
                longestSubL = tempL
        return longestSubL
