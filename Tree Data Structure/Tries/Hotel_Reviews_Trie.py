class Solution:
    # @param S : string, good words
    # @param R : list of strings, individual reviews
    # @return a list of integers
    def trieCreation(self, S):
        n = len(S)
        good_words = dict()
        for i in range(n):
            try:
                good_words[S[i][0]]
            except:
                good_words[S[i][0]] = dict()
            curr = good_words[S[i][0]]
            temp = good_words[S[i][0]]
            j, m = 1, len(S[i])
            while j < m:
                try:
                    curr[S[i][j]]
                except:
                    curr[S[i][j]] = dict()
                temp = curr[S[i][j]]
                curr = temp
                j += 1
            curr["."] = True
        return good_words

    def solve(self, S, R):
        S = S.split("_")
        good_words = self.trieCreation(S)
        reviews = [review.split("_") for review in R]
        n = len(R)
        rating = [0] * n
        for i in range(n):
            for word in reviews[i]:
                tester = good_words
                reject = False
                for j in range(len(word)):
                    try:
                        tester[word[j]]
                        tester = tester[word[j]]
                    except:
                        reject = True
                        break
                if not reject: 
                    try:
                        if tester["."]: rating[i] += 1
                    except:
                        pass
        output = [i for i in range(n)]
        return sorted(output, key = lambda i: rating[i], reverse = True)
