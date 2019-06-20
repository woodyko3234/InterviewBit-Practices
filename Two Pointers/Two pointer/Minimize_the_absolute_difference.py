class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, A, B, C):
	    n,m,l = len(A), len(B), len(C)
	    i, j, k = 0,0,0
	    diff = 2**31 - 1
	    while i < n and j < m and k < l and diff > 0:
	        maxCurr, minCurr = max(A[i], B[j], C[k]), min(A[i], B[j], C[k])
	        if abs(maxCurr - minCurr) < diff:
	            diff = abs(maxCurr - minCurr)
	        if A[i] == minCurr: i += 1
	        elif B[j] == minCurr: j += 1
	        else: k += 1
	    return diff
