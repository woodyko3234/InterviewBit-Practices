class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        occupancy = 0
        n = len(arrive)
        if n == 1:
            if K > 0: return True
            else: return False
        elif n == 0: return True
        arrive = sorted(arrive)
        depart = sorted(depart)
       
        i, j = 0, 0
        while i < n and j < n:
            if arrive[i] < depart[j]:
                occupancy += 1
                if occupancy > K: return False
                i += 1
            else:
                occupancy -= 1
                j += 1
        return True
'''
class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
        events = sorted(events)

        guests = 0

        for event in events:
            if event[1] == 1:
                guests += 1
            else:
                guests -= 1

            if guests > K:
                return 0

        return 1
'''
