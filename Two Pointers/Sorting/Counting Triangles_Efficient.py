class Solution:
	# @param A : list of integers
	# @return an integer
	def nTriang(self, A):
	    """
	    constrains
	    a <= b <= c
	    a + b > c
	    """
	    n, triForms = len(A), 0
	    sortA = sorted(A, reverse = True)
	    for i in range(n-2):
	        c_idx = i
	        a_idx, b_idx = n-1, c_idx + 1
	        while a_idx > b_idx:
	            if sortA[a_idx] + sortA[b_idx] > sortA[c_idx]:
	                triForms += (a_idx - b_idx)
	                b_idx += 1
	            else: a_idx -= 1
	        ###O(n^3) method
	        #for j in range(i+1, n-1):
	        #    for k in range(j+1, n):
	        #        if sortA[i] + sortA[j] > sortA[k]:
	        #            triForms += 1
	    return triForms % 1000000007
	    
