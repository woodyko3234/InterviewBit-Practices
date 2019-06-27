class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
	    n = len(A)
	    i = 0
	    j = i + 1
	    if B > 0:
	        neg = 1
	    else: neg = -1
	    while j < n:
	        if neg * (A[j] - A[i]) == B: return 1
	        else:
	            diff = (A[j] - A[i]) - (neg * B)
	            if diff < 0: 
	                if j < n-1:
	                    j += 1
	                else: return 0
	            elif i == j - 1:
	                j += 1
	                i += 1
	            else: i += 1
	    ###O(n^2) method
	    #for i in range(n-1):
        #    for j in range(i+1, n):
        #        if abs(A[i] - A[j]) == abs(B): return 1
        return 0
