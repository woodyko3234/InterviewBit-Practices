class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, A, B):
            
        retlist = []
        if (A < 0) ^ (B < 0) and (A != 0):
            retlist.append('-')
        A = abs(A)
        B = abs(B)
        retlist.append(str(A//B))
        if A%B:
            retlist.append('.')
        hashmap = {}
        # 44/30 ---- 1 . 14%30 - 14 
        rem = A % B
        while  rem and  rem not in hashmap:
            hashmap[rem] = len(retlist) - 1
            rem = 10 * rem 
            retlist.append(str(rem // B))
            rem = rem % B
        if rem:
            retlist.insert(hashmap[rem]+1, '(')
            retlist.append(')')
        return ''.join(val for val in retlist)
