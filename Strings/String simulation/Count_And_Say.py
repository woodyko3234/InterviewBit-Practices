class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A <= 1:
            return str(A)
        elif A == 2:
            return '11'
        else:
            prior = '11'
            for i in range(3, A+1):
                next_count = []
                count = 0
                for j in range(len(prior)):
                    if j - 1 < 0 or prior[j] == prior[j-1]: pass
                    
                    elif prior[j] != prior[j-1]:
                        next_count.append(str(count))
                        count = 0
                        next_count.append(prior[j-1])
                
                    count += 1
                    if j == (len(prior) - 1):
                        next_count.append(str(count))
                        next_count.append(prior[j])
                prior = ''.join(next_count)
        return prior
