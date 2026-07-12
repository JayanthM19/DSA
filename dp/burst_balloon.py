#https://leetcode.com/problems/burst-balloons/
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Watch dp51 video bruh , u cant solve this alone
        n=len(nums)

        nums.insert(0,1)
        nums.append(1)

#Recursion

        # def solve(i,j):
        #     if i>j:    #Check this line
        #         return 0
            
        #     maxi = 0
        #     for ind in range(i,j+1):
        #         cost=(nums[i-1]*nums[ind]*nums[j+1])+ solve(i,ind-1) + solve(ind+1,j)

        #         maxi=max(cost,maxi)

        #     return maxi
            

        # return solve(1,n)

#Memoization

        # dp=[[-1]*(n+1) for _ in range(n+1)]
        # def solve(i,j):
        #     if i>j:    #Check this line
        #         return 0
            
        #     if dp[i][j]!=-1:
        #         return dp[i][j]

        #     maxi = 0
        #     for ind in range(i,j+1):
        #         cost=(nums[i-1]*nums[ind]*nums[j+1])+ solve(i,ind-1) + solve(ind+1,j)

        #         maxi=max(cost,maxi)

        #     dp[i][j]=maxi

        #     return dp[i][j]
            

        # return solve(1,n)

#Tabulation

        dp=[[0]*(n+2) for _ in range(n+2)]

        for i in range(n,0,-1):
            for j in range(i,n+1):
                
                if i>j:
                    continue
                
                maxi=0
                for ind in range(i,j+1):
                    cost=(nums[i-1]*nums[ind]*nums[j+1]) + dp[i][ind-1] + dp[ind+1][j]

                    maxi=max(maxi,cost)

                dp[i][j]=maxi
        
        return dp[1][n]
                

