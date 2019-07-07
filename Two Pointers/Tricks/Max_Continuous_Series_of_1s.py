class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, bits, num):
        for i in range(len(bits)):
            bits[i] = str(bits[i])
        combined_bits = "".join(bits)
        split_zero = combined_bits.split("0")
        ones_count = [len(i) for i in split_zero]
    
        #need one flip to connect 2 adjacent items
        left_most = 0
        max_ones = len(split_zero[0])
        max_left = 0     #the left most idx in split_zero
        max_right = 0    #the right most idx in split_zero
    
        idx = 0
        flips = 0
        cur_connects = ones_count[0]
        while idx < len(split_zero) - 1:
            if flips < num:
                flips += 1
                cur_connects = cur_connects + 1 + ones_count[idx + 1]
                #max_ones = max(max_ones, cur_connects)
                #need to keep track of left and right borders when max_ones is found
                if cur_connects > max_ones:
                    max_ones = cur_connects
                    max_left = left_most
                    max_right = idx+1
                
            else:
                cur_connects = cur_connects + len(split_zero[idx + 1]) - len(split_zero[left_most])
                left_most += 1
                if cur_connects > max_ones:
                    max_ones = cur_connects
                    max_left = left_most
                    max_right = idx+1
            idx += 1
        #the while loop counts the max_ones correctly 
        #finally, return the idx range
        cur_pos_accumulated = 0
        for i in range(len(ones_count)):
            if max_left == i:
                left_idx = cur_pos_accumulated
            cur_pos_accumulated += ones_count[i]
            if max_right == i:
                right_idx = cur_pos_accumulated
            if i == (len(ones_count) - 1): pass
            else: cur_pos_accumulated += 1
        return [i for i in range(left_idx, right_idx)]
