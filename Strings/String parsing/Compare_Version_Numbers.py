class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        a_split = A.split('.')
        b_split = B.split('.')
        min_len = min(len(a_split), len(b_split))
            
        for i in range(min_len):
            if int(a_split[i]) > int(b_split[i]): return 1
            elif int(a_split[i]) < int(b_split[i]): return -1
        
        if len(a_split) > len(b_split):
            for j in range(min_len, len(a_split)):
                if int(a_split[j]) > 0:
                    return 1
            return 0
        elif len(a_split) < len(b_split): 
            for j in range(min_len, len(b_split)):
                if int(b_split[j]) > 0:
                    return -1
            return 0
        else: return 0
