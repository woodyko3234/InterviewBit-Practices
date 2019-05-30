class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def addBinary(self, A, B):
	    bin_A, bin_B = int(A), int(B)
	    com_bin = bin_A + bin_B
	    update_bin = ""
	    plus_one = False
	    for i in str(com_bin)[::-1]:
	        if i == "2" and plus_one:
	            update_bin = "1" + update_bin
	        elif i == "2" or (i == "1" and plus_one):
	            update_bin = "0" + update_bin
	            plus_one = True
	        else:
	            update_bin = str(int(i) + plus_one) + update_bin
	            plus_one = False
	    if plus_one:
	        update_bin = "1" + update_bin
	    return update_bin
