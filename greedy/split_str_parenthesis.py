#https://leetcode.com/problems/split-a-string-in-balanced-strings/
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        left=0

        for sub in s:
            if sub=='L':
                left+=1
            else:
                left-=1
            
            if not left:
                ans+=1
        
        return ans