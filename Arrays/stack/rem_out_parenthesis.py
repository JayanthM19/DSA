#https://leetcode.com/problems/remove-outermost-parentheses/

class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        level=0

        for ch in s:
            if ch=='(':
                if level>0:
                    res+=ch
                
                level+=1
            else:
                level-=1
                if level>0:
                    res+=ch
        
        return res