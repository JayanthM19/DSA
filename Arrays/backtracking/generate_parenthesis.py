#https://leetcode.com/problems/generate-parentheses/

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        final=[]

        def solve(open,close,curr):

            if len(curr)==2*n:
                final.append(curr)
                return
            
            if open < n :
                solve(open+1,close,curr+"(")
            
            if close<open:
                solve(open,close+1,curr+")")

        solve(0,0,"")
        return final