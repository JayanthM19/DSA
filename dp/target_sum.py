#https://leetcode.com/problems/target-sum/

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        n=len(nums)
#Recursion Method
        # def solve(ind ,curr):
            
        #     if ind<0:
        #         return 1 if curr==target else 0

        #     add = solve(ind-1,curr+nums[ind])
        #     sub = solve(ind-1,curr-nums[ind])

        #     return add+sub
            
        # return solve(n-1,0)

#Memoization

        # dp={}

        # def solve(ind,curr):
            
        #     if ind<0:
        #         return 1 if curr==target else 0
            
        #     if (ind,curr) in dp:
        #         return dp[(ind,curr)]
            
        #     add = solve(ind-1,curr+nums[ind])
        #     sub = solve(ind-1,curr-nums[ind])
            

        #     dp[(ind,curr)]=add+sub

            
        #     return dp[(ind,curr)]
        
        # return solve(n-1,0)

#Tabulation
        #Say s1 have all + and s2 have all - 
        #then s1+s2=sum(nums)
        #s1-s2=target
        #s1=target+s2
        #so , target+2s2=sum(nums)
        #s2=sum(nums)-target / 2
        #f(ind , s2)


        total = sum(nums)

        if abs(target)>total :
            return 0

        if (total-target)%2!=0:
            return 0

        s2=(total-target)//2

        # dp=[[0]*(s2+1) for _ in range(n+1)]

        # dp[0][0]=1

        # for i in range(1,n+1):
        #     for j in range(s2+1):
        #         nottake=dp[i-1][j]

        #         take=0
        #         if nums[i-1]<=j:
        #             take=dp[i-1][j-nums[i-1]]

        #         dp[i][j]=take+nottake

        # return dp[n][s2] 

#Space optimization

        prev=[0]*(s2+1)

        prev[0]=1

        for i in range(1,n+1):
            curr=[0]*(s2+1)
            curr[0]=1
            for j in range(s2+1):
                nottake=prev[j]

                take=0
                if nums[i-1]<=j:
                    take=prev[j-nums[i-1]]

                curr[j]=take+nottake
            
            prev=curr
        
        return prev[s2]
                

        
        

        

