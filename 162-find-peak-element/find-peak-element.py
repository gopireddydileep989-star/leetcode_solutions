class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            m = max(nums)
            if m==nums[i]:
                return i