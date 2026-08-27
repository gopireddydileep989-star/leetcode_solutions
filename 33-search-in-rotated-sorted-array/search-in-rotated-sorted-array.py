class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans=0
        for i in range(len(nums)):
            if nums[i]==target:
                return ans
            else:
                ans+=1
        return -1