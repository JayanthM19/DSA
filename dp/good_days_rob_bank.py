#https://leetcode.com/problems/find-good-days-to-rob-the-bank/

class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        n=len(security)
        down=[1]*n
        up=[1]*n


        for i in range(1,n):
            if security[i]<=security[i-1]:
                down[i]=1+down[i-1]

        for i in range(n-2,-1,-1):
            if security[i]<=security[i+1]:
                up[i]=1+up[i+1]

        ans=[]
        for i in range(n):
            if up[i]>=time+1 and down[i]>=time+1:
                ans.append(i)

        return ans
