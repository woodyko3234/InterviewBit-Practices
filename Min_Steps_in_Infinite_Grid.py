class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        if len(X) == 0 or len(Y) == 0 or len(X) != len(Y): return 0
        start_pos = (X[0], Y[0])
        steps = 0
        for x, y in zip(X[1:], Y[1:]):
            x_dif = abs(x - start_pos[0])
            y_dif = abs(y - start_pos[1])
            steps += max(x_dif, y_dif)
            start_pos = (x,y)
        return steps
