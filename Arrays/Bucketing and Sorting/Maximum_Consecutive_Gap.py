class Solution:
    def maximumGap(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 2:
            return 0

        min_v, max_v = min(arr), max(arr)
        if max_v - min_v < 2:
            return max_v - min_v

        min_gap = max(1, (max_v - min_v) // (len(arr)-1))  # The minimum possible gap
        sentinel_min, sentinel_max = 2 ** 32 - 1, -1
        buckets_min = [sentinel_min] * len(arr)
        buckets_max = [sentinel_max] * len(arr)

        for x in arr:
            i = min((x - min_v) // min_gap, len(arr) - 1)
            buckets_min[i] = min(buckets_min[i], x)
            buckets_max[i] = max(buckets_max[i], x)
        max_gap = 0
        prev_max = buckets_max[0]  # First gap is always non-empty
        for i in range(1, len(arr)):
            if buckets_min[i] == sentinel_min:
                continue
            max_gap = max(buckets_min[i] - prev_max, max_gap)
            prev_max = buckets_max[i]

        return max_gap
