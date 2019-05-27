class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        a_split = A.split(' ')
        idx = 0
        while idx < len(a_split):
            if a_split[idx] == '':
                a_split.pop(idx)
            else:
                idx += 1
        
        a_len = len(a_split)
        
        if a_len == 0: return ""
        elif a_len == 1: return a_split[0]
        else:
            for i in range(0, int(a_len / 2)):
                a_split[i], a_split[(a_len-1)-i] = a_split[(a_len-1)-i], a_split[i]
        
        return " ".join(a_split)
