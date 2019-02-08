class Solution:
	# @param A : integer
	# @return a list of integers
	def primeUpdate(self, A):
	    output = [True]*(A+1)
	    output[0], output[1] = False, False
	    for i in range(4, A+1, 2):
	        output[i] = False
	    for i in range(3, int(pow(A, 0.5))+1, 2):
	        for j in range(i*2, A+1, i):
	            output[j] = False
	    return output
	
	def primesum(self, A):
	    if A == 4: return [2,2]
	    prime_statues = self.primeUpdate(A)
	    for i in range(3, A, 2):
	        if prime_statues[i] and prime_statues[A-i]:
	            return [i, A-i]
