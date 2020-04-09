from collections import defaultdict
class Solution:
    # @param S : string, good words
    # @param R : list of strings, individual reviews
    # @return a list of integers
    def solve(self, S, R):
        S = S.split("_")
        good_words = defaultdict(bool)
        for s in S:
            good_words[s] = True
        reviews = [review.split("_") for review in R]
        n = len(R)
        rating = [0] * n
        for i in range(n):
            for word in reviews[i]:
                if good_words[word]:
                    rating[i] += 1
        
        output = [i for i in range(n)]
        return sorted(output, key = lambda i: rating[i], reverse = True)
