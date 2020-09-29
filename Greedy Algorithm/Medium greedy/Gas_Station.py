class Solution:
    # @param gas : tuple of integers
    # @param cost : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        '''The bruteforce solution should be obvious. Start from every i, 
        and check to see if every point is reachable with the gas available. 
        Return the first i for which you can complete the trip without the gas reaching 
        a negative number. 
        This approach would however be quadratic.
        Lets look at how we can improve. 
        
        1) If sum of gas is more than sum of cost, 
        does it imply that there always is a solution ? 
        2) Lets say you start at i, and hit first negative of 
        sum(gas) - sum(cost) at j. We know TotalSum(gas) - TotalSum(cost) > 0. 
        What happens if you start at j + 1 instead ? 
        Does it cover the validity clause for i to j already ?'''
        gas_left = gas_needed = start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            gas_left += g - c
            if gas_left < 0:
                gas_needed -= gas_left
                start = i + 1
                gas_left = 0
        return start if gas_left >= gas_needed else -1
