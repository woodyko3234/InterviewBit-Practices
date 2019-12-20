class Solution:
	# @param A : list of integers
	# @return a list of integers
	def lszero(self, A):
	    """
	    Find j - i maximized with sum(A[i:j]) == 0
	    sum(A[i:j]) == 0 => sum(A[:j]) = sum(A[:i-1])
	    """
	    hashSum = {0:-1}
	    temp, maxL, comb = 0, 0, []
	    for i in range(len(A)):
	        temp += A[i]
	        try:
	            if ((i+1) - hashSum[temp] > maxL):
	                maxL = (i+1) - hashSum[temp]
	                comb = A[hashSum[temp]+1:i+1]
	        except:
	            hashSum[temp] = i
        return comb
