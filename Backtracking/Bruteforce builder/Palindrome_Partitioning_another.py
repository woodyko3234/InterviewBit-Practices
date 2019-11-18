class Solution:
    # @param A : string
    # @return a list of list of strings
    def __init__(self):
        self.dic = {}
    def isP(self, string):
        return string[::-1] == string
    
    def partition(self, A):
        ans = []
        if len(A) <= 1:
            return [A]
        if A in self.dic:
            return self.dic[A]
        for index, i in enumerate(A):
            cur_st = A[:index+1]
            l = [cur_st]
            if self.isP(cur_st):
                temp = self.partition(A[index+1:])
                for i in temp:
                    l = [cur_st]
                    l.extend(i)
                    ans.append(l)
        self.dic[A] = ans
        return ans
