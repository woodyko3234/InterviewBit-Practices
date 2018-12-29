class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        if len(A) == 0: return []
        start_pos = 0
        maximum = 0
        max_list = []
        last_neg_pos = -1
        current_list = []
        current_max = 0
        for idx, num in enumerate(A):
            if num >= 0 and idx - last_neg_pos == 1:
                start_pos = idx
                current_max += num
                current_list.append(num)
            elif num >= 0:
                current_max += num
                current_list.append(num)
            else:
                last_neg_pos = idx
                if maximum < current_max:
                    maximum = current_max
                    max_list = current_list
                elif maximum == current_max and len(max_list) < len(current_list):
                    max_list = current_list
                current_max = 0
                current_list = []
        if maximum < current_max:
            max_list = current_list
        elif maximum == current_max and len(max_list) < len(current_list):
            max_list = current_list
        return max_list
