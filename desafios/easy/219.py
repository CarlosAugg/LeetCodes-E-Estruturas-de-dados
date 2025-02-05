class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}

        for idx, x in enumerate(nums):
            if x in d and abs(idx - d[x] ) <= k:
                    return True
            else:
                d[x] = idx

        return False