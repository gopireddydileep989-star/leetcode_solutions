class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(16):
            a = 4 ** i
            if a == n:
                return True
            if a > n:
                return False
        return False
