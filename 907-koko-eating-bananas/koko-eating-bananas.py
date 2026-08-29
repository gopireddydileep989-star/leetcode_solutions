class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            k = (l + r) // 2
            hr = 0
            for i in piles:
                hr += (i + k - 1) // k
            if hr <= h:
                r = k
            else:
                l = k + 1  
        return l