class Solution:
    # @param s : string
    # @return a list of list of strings
    def isPalindrome(self, sub):
        #sub == sub[::-1]
        l = len(sub)
        for i in range(l//2):
            if sub[i] != sub[l-1-i]:
                return False
        return True
    
    def partition(self, s):
        def recur(sub, res, cur):
            if len(sub)==0:
                res+=[cur]
            else:
                for i in range(1, len(sub)+1):
                    if self.isPalindrome(sub[:i]):
                        recur(sub[i:], res, cur+[sub[:i]])
        res = []
        recur(s, res, [])
        return res
