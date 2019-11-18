class Solution:
	# @param A : integer
	# @return a list of strings
	def generateParenthesis(self, A):
	    ptsComb = []
	    if A == 0: return ptsComb
	    leftPts, rightPts = 0, 0
	    
	    def recursive(leftPts, rightPts, A, curr):
	        if rightPts == A:
                ptsComb.append(curr)
	        elif leftPts == rightPts:
	            recursive(leftPts+1, rightPts, A, curr + "(")
	        elif leftPts < A:
	            recursive(leftPts+1, rightPts, A, curr + "(")
	            recursive(leftPts, rightPts + 1, A, curr + ")")
	        elif rightPts < A:
	            recursive(leftPts, rightPts+1, A, curr + ")")
	    
	    recursive(leftPts, rightPts, A, "")
	    return ptsComb
