from collections import defaultdict
class Solution:
    # @param S : list of integers
    # @param T : integer
    # @return a list of list of integers
    def fourSum(self, S, T):
        #since condition a<=b<=c<=d must be applied
        S.sort()
        sumMatch = defaultdict(list)
        n, output = len(S), []
        for i in range(n-3):
            for j in range(i+1, n-2):
                #T-(S[i]+S[j]) == S[k]+S[l]
                if [S[i], S[j]] in sumMatch[T-S[i]-S[j]]:
                    continue
                sumMatch[T-S[i]-S[j]].append([S[i], S[j]])
                target = T-S[i]-S[j]
                k, l = j+1, n-1
                while k < l:
                    if target-S[k]-S[l] > 0:
                        k += 1
                    elif target-S[k]-S[l] < 0:
                        l -= 1
                    else:
                        output.append([S[i],S[j],S[k],S[l]])
                        while S[k] == S[k+1] and k+1 < l:
                            k += 1
                        while S[l] == S[l-1] and l-1 > k:
                            l -= 1
                        k += 1
                        l -= 1
        return output
