class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canfinish(cap):
            day  = 1
            load = 0
            for i in weights:
                load += i
                if load > cap:
                    day += 1
                    load = i
            return day
        l = max(weights)
        h = sum(weights)
        ans = h
        while l<=h:
            mid = (l+h)//2
            total = canfinish(mid)
            if total<=days:
                ans = mid
                h = mid-1
            else:
                l = mid+1
        return ans