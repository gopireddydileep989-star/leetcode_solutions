class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l = []
        l1 = []
        for i in s:
            if i != '#':
                l.append(i)
            elif l:
                l.pop()
        for j in t:
            if j != '#':
                l1.append(j)
            elif l1:
                l1.pop()
        return l == l1