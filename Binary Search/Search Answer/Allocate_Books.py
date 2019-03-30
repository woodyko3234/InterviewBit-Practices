class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, A, B):
	    best = max(A)
	    worst = sum(A)
	    if B == 1: return worst
	    elif B < 1 or B > len(A): return -1
	    while best < worst:
	        mid = (best + worst) // 2
	        students = self.studentCounts(A, mid)
	        if students > B:
	            best = mid + 1
	        else:
	            worst = mid
        return worst
	    
	def studentCounts(self, A, mid):
	    students = 1
	    pages = 0
	    for p in A:
	        if pages + p <= mid:
	            pages += p
            else:
                students += 1
                pages = p
        return students
