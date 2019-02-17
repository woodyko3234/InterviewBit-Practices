class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        #if A = 1=> chr(a) = chr(1 + 64) = 'A'
        chars = []
        while A > 0:
            if A%26 != 0:
                chars.append(chr(A%26 + 64))
                A = A//26
            else:
                chars.append(chr(26 + 64))
                A = A//26 - 1
        return "".join(chars[::-1])
