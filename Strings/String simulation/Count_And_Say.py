class Solution:
	# @param A : integer
	# @return a string
	def countAndSay(self, A):
	    if A == 0: return ""
	    elif A < 0 or A == 1: return "1"
	    current = "1"
	    for i in range(1, A):
	        counts, temp = 0, ""
	        temp_s = ""
	        for w in current:
	            if temp == w: counts += 1
	            elif counts == 0: 
	                temp = w
	                counts = 1
	            else:
	                temp_s = temp_s + str(counts) + temp
	                temp = w
	                counts = 1
	        temp_s = temp_s + str(counts) + temp
	        current = temp_s
	    return current
