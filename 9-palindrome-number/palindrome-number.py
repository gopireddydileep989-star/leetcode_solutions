class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        input_num = x
        newnum = 0
        while x>0:
            newnum = newnum*10+x%10
            x = x//10
        return newnum == inputnum
        
