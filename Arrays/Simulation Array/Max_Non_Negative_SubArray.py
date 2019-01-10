class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        n = len(A)
        if n == 0: return []
        maximum, current_max =0, 0
        max_list, current_list = [], []
        for i in range(n):
            if A[i] >= 0: 
                current_list.append(A[i])
            else:
                current_max = sum(current_list)
                if current_max > maximum or (current_max == maximum and len(current_list)>len(max_list)):
                    maximum = current_max
                    max_list = current_list
                current_list = []
        current_max = sum(current_list)
        if current_max > maximum or (current_max == maximum and len(current_list)>len(max_list)):
            maximum = current_max
            max_list = current_list
        return max_list
