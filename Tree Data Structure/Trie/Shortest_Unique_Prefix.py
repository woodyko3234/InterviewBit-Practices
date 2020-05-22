from collections import defaultdict
class Node:
    def __init__(self, x):
        self.key = x[0]
        self.value = 1
        self.child = defaultdict(list)



class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        self.wordTrie = defaultdict(list)
        for w in A:
            #create trie
            self.trieCreation(w, self.wordTrie)
        
        output = []
        for w in A:
            #find unique prefix
            idx = 0
            curr = self.wordTrie[w[idx]]
            while idx < len(w)-1:
                if curr[0] == 1:
                    break
                idx += 1
                curr = curr[1][w[idx]]
            output.append(w[:idx+1])
        return output

    def trieCreation(self, w, tries):
        trie = Node(w)
        try:
            tries[trie.key][0] += trie.value
        except:
            tries[trie.key].append(trie.value)
            tries[trie.key].append(trie.child)
        if len(w) == 1: return 
        return self.trieCreation(w[1:], tries[trie.key][1])
