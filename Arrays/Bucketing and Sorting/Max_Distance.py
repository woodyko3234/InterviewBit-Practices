class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) == 0:
            return -1
        # arr[i][j] = max distance starting from i and including up to j
        index = list(range(len(A)))
        index.sort(key=lambda x: A[x])
        largest_distance = 0
        max_index_from_i = [index[-1]] * len(A)
        i = len(A) - 2
        while i >= 0:
            max_index_from_i[i] = max(max_index_from_i[i+1], index[i])
            i -= 1
        print(max_index_from_i)
        for i in range(len(A) - 1):
            largest_distance = max(largest_distance, max_index_from_i[i] - index[i])
        if largest_distance <= 0:
            return 0
        else:
            return largest_distance
