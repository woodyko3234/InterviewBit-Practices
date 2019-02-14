class Solution:
    # @param A : string
    # @return an integer
    def fact (self, n ) :
        if n <= 1 :
            return 1
        else :
            return n * self.fact(n-1)

    def findRank(self, A):
        res = 1
        char_occur = {}
        for char in A:
            char_occur[char] = char_occur.get(char, 0) + 1
        for i in range(0, len(A)-1) :
            rank = 0
            for j in range(i+1, len(A)) :
                if A[i] > A[j] :
                    rank += 1
            temp = self.fact(len(A) - i - 1)%1000003
            temp1= 1
            for key in char_occur.keys() :
                temp1 *= self.fact(char_occur[key])
            temp1 = pow(temp1, 1000001, 1000003)
            res = (res + rank * temp1 * temp)%1000003
            char_occur[A[i]] -= 1
        return res
