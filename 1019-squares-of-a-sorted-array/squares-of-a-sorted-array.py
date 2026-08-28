class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        li = []
        for i in nums:
            m = i*i
            li.append(m)
        return sorted(li)
        