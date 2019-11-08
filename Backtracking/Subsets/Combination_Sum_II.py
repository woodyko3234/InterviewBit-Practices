class Solution:
    # @param c : list of integers
    # @param t : integer
    # @return a list of list of integers
    def __init__(self):
        self.output = []
        
    def sortList(self, c):
        return sorted(c)
    
    def combinationSum(self, c, t, pos = 0, temp = None):
        temp = temp or []
        c = self.sortList(c)
        if self.output and temp[:] == self.output[-1]: return 
        elif t == 0:
            self.output.append(temp[:])
            return 
        elif t < 0:
            return 
        for i in range(pos, len(c)):
            temp.append(c[i])
            self.combinationSum(c, t-c[i], i+1, temp)
            temp.pop()
        return self.output
