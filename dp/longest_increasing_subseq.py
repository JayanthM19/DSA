#https://leetcode.com/problems/longest-increasing-subsequence/
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#Recursion
        n=len(nums)

        # def solve(ind,prev_ind):

        #     if ind==n:
        #         return 0
            
        #     nottake = 0+solve(ind+1,prev_ind)

        #     take=0
        #     if prev_ind==-1 or nums[ind]>nums[prev_ind]:
        #         take = 1 + solve(ind+1,ind)
            
        #     return max(take,nottake)
        # return solve(0,-1)

#Memoization
        # dp=[[-1]*(n+1) for _ in range(n)]

        # def solve(ind,prev_ind):

        #     if ind==n:
        #         return 0
            
        #     if dp[ind][prev_ind]!=-1:
        #         return dp[ind][prev_ind]
            
        #     nottake = 0+solve(ind+1,prev_ind)

        #     take=0
        #     if prev_ind==-1 or nums[ind]>nums[prev_ind]:
        #         take = 1 + solve(ind+1,ind)
            
        #     dp[ind][prev_ind]=max(take,nottake)
        #     return dp[ind][prev_ind]
        # return solve(0,-1)

#Tabulation

        # dp=[[0]*(n+1) for _ in range(n+1)]

        # for i in range(n-1,-1,-1):
        #     for j in range(i-1,-2,-1):
        #         nottake = 0+dp[i+1][j+1]
        #         take=0
        #         if j==-1 or nums[i]>nums[j]:
        #             take=1+dp[i+1][i+1]

        #         dp[i][j+1]=max(take,nottake)
        
        # return dp[0][0]

#Space Optimization

        
        # ahead=[0]*(n+1)


        # for i in range(n-1,-1,-1):
        #     curr=[0]*(n+1)
        #     for j in range(i-1,-2,-1):
        #         nottake = 0+ahead[j+1]
        #         take=0
        #         if j==-1 or nums[i]>nums[j]:
        #             take=1+ahead[i+1]

        #         curr[j+1]=max(take,nottake)
            
        #     ahead=curr
        
        # return ahead[0]

#Better Optimal

        dp=[1]*n

        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(1+dp[j],dp[i])
        
        return max(dp)

