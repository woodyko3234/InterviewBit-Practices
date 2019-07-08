class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def maxone(self, A, B):
	    n = len(A)
	    onesCounter, ones = [], 0
	    for i in range(n):
	        if A[i] == 1: ones += 1
	        else:
	            onesCounter.append(ones + 1)
	            ones = 0
	    curr, max_len = 0,0
	    max_pos, flips, to_drop = 0, 0, 0
	    for i in range(n):
	        if A[i] == 1:
	            curr += 1
	        else:
	            if flips < B: flips += 1
	            else:
	                curr -= onesCounter[to_drop]
	                to_drop += 1
                curr += 1
	        if curr > max_len:
                max_len = curr
                max_pos = i
	    return list(range(max_pos - max_len + 1, max_pos + 1))
