class Solution:
	# @param string : string
	# @param pattern : string
	# @return an integer
	def getLPS(self, pattern, m):
	    lps = [0]*(m)
	    i, j = 1, 0
	    while i < m:
	        if pattern[i] == pattern[j]:
	            j += 1
	            lps[i] = j
	            i += 1
	        elif j != 0:
	            j = lps[j-1]
	        else:
	            i += 1
	    return lps
	def strStr(self, string, pattern):
	    n,m = len(string), len(pattern)
	    if n == 0 or m == 0: return -1
	    i, j = 0,0
	    lps = self.getLPS(pattern, m)
	    while i < n and j < m:
	        if string[i] == pattern[j]:
	            i += 1
	            j += 1
	        elif j != 0:
	            j = lps[j - 1]
	        else:
	            i += 1
	    if j == m: return i - m
	    else: return -1
