class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        m_a = 0
        while i<j:
            a = (j-i) * min(height[i],height[j])
            m_a = max(m_a,a)
            if height[i] < height[j]:
                i += 1
            elif height [j] < height[i]:
                j -= 1
            else:
                i += 1
                j -= 1
        return m_a