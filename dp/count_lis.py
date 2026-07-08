#https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[1]*n
        count=[1]*n

        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    if dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
                        count[i]=count[j]
                    elif dp[i]==dp[j]+1:
                        count[i]+=count[j]

        maxLen=max(dp)
        ans=0

        for i in range(n):
            if dp[i]==maxLen:
                ans+=count[i]

        return ans

        
        


        

        
