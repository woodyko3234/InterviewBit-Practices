class Solution:
    # @param s : string
    # @return a list of strings
    def __init__(self):
        #build the mapping dict
        self.numPad = {"0": ["0"], "1": ["1"], "2": ["a", "b", "c"],
                     "3": ["d", "e", "f"], "4": ["g", "h", "i"], 
                     "5": ["j", "k", "l"], "6": ["m", "n", "o"],
                     "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"],
                     "9": ["w", "x", "y", "z"]}

    def letterCombinations(self, s):
        comb = []
        temp = ""
        def recursive(temp, s):
            if len(s) > 1:
                for i in self.numPad[s[0]]:
                    recursive(temp + i, s[1:])
            else:
                for i in self.numPad[s[0]]:
                    comb.append(temp + i)
        recursive(temp, s)
        return comb
