class Solution:
    # @param S : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, S):
        """
        Your Input: 7 1 1 2 2 3 3 3
        Expected output is [] [1 ] [1 1 ] [1 1 2 ] [1 1 2 2 ] [1 1 2 2 3 ] 
        [1 1 2 2 3 3 ] [1 1 2 2 3 3 3 ] [1 1 2 3 ] [1 1 2 3 3 ] [1 1 2 3 3 3 ] 
        [1 1 3 ] [1 1 3 3 ] [1 1 3 3 3 ] [1 2 ] [1 2 2 ] [1 2 2 3 ] [1 2 2 3 3 ] 
        [1 2 2 3 3 3 ] [1 2 3 ] [1 2 3 3 ] [1 2 3 3 3 ] [1 3 ] [1 3 3 ] [1 3 3 3 ] 
        [2 ] [2 2 ] [2 2 3 ] [2 2 3 3 ] [2 2 3 3 3 ] [2 3 ] [2 3 3 ] [2 3 3 3 ] 
        [3 ] [3 3 ] [3 3 3 ]
        """
        output = []
        S.sort()
        def recursive(S, sub_set, i):
            output.append(sub_set)
            for j in range(i, len(S)):
                if i != j and S[j-1] == S[j]:
                    continue
                recursive(S, sub_set + [S[j]], j+1)
            
        recursive(S, [], 0)
        return output
