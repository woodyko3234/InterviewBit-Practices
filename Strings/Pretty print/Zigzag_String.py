class Solution:
    # @param A : string
    # @param B : integer
    # @return a string
    def convert(self, A, B):
        if B <= 1: return A
        zigzagStrings = [[] for _ in range(B)]
        cur, backtrack = 0, False
        for c in A:
            if cur < B and backtrack == False:
                zigzagStrings[cur].append(c)
                cur += 1
            elif cur == B and backtrack == False:
                backtrack = True
                cur -= 2
                zigzagStrings[cur].append(c)
            elif cur > 0 and backtrack == True:
                cur -= 1
                zigzagStrings[cur].append(c)
            elif cur == 0 and backtrack == True:
                backtrack = False
                cur += 1
                zigzagStrings[cur].append(c)
                cur += 1
            #print(zigzagStrings, cur)
        for i in range(B):
            zigzagStrings[i] = "".join(zigzagStrings[i])
        return "".join(zigzagStrings)
                
