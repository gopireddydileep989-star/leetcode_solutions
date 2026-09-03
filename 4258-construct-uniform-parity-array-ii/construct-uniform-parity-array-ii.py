class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = min(nums1)
        if mn & 1:
            return True
        for n in nums1:
            if n & 1:
                return False
        return True