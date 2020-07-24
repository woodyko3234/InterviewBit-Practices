
class LRUCache:

    def __init__(self, capacity):
        self.pairs = dict()
        self.capacity = capacity
        #recording command orders
        self.orderKey = dict()
        self.keyOrder = dict()
        self.orderNum = 10000
        self.orderLimit = 10000

    def get(self, key):
        try:
            v = self.pairs[key]
            self.orderKey.pop(self.keyOrder.pop(key))
            self.keyOrder[key] = self.orderNum
            self.orderKey[self.orderNum]  = key
            self.orderNum -= 1
            return v
        except:
            return -1

    def set(self, key, value):
        try:
            self.pairs.pop(key)
            self.orderKey.pop(self.keyOrder.pop(key))
        except:
            if len(self.pairs) >= self.capacity:
                while True:
                    keyToDrop = self.orderKey.pop(self.orderLimit, -1)
                    self.orderLimit -= 1
                    if keyToDrop == -1: continue
                    self.pairs.pop(keyToDrop)
                    self.keyOrder.pop(keyToDrop)
                    break
        self.pairs[key] = value
        self.keyOrder[key] = self.orderNum
        self.orderKey[self.orderNum]  = key
        self.orderNum -= 1
