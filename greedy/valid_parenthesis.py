#https://leetcode.com/problems/valid-parenthesis-string/

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #low --> min possible open brackets
        #high --> max possible open brackets

        low,high=0,0

        for su in s:
            if su=="(":
                low+=1
                high+=1
            
            elif su==")":
                low-=1
                high-=1
            
            else: # *
                low-=1
                high+=1
            
            if high<0:
                return False
            
            low=max(low,0)

        return low==0