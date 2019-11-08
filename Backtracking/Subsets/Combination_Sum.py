class Solution:
    # @param c : list of integers
    # @param t : integer
    # @return a list of list of integers
    def __init__(self):
        self.output = []
        
    def sortList(self, c):
        return sorted(list(set(c)))
        
    def combinationSum(self, c, t, pos = 0, temp = None):
        temp = temp or []
        c = self.sortList(c)
        
        if t == 0: 
            self.output.append(temp[:])
            return 
        elif t < 0:
            return
        else:
            for i in range(pos, len(c)):
                temp.append(c[i])
                self.combinationSum(c, t-c[i], i, temp)
                temp.pop()
        return self.output
