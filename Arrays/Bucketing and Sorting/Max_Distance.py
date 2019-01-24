class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) == 0:
            return -1
        arr = []
        # add index info into the array
        for idx, v in enumerate(A):
            arr.append([v, idx])
        arr.sort()
        #[ 5, 3, 11 ] => [[3, 1], [5, 0], [11, 2]]
        cur_idx = arr[0][1]
        max_diff = -1
        for j in arr:
            if j[1] < cur_idx:
                #replace
                cur_idx = j[1]
            else:
                if  j[1] - cur_idx > max_diff:
                    max_diff = j[1] - cur_idx
        return max_diff
