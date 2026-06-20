#https://leetcode.com/problems/perfect-squares/description/

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        
        k=int(n**(0.5))
        

        nums=[]
        for i in range(1,k+1):
            nums.append(i*i)
        
        w=len(nums)
        #dp=[[float('inf')]*(n+1) for _ in range(w)]
        

        # for i in range(n+1):
        #     dp[0][i]=i
        prev=[0]*(n+1)
        for j in range(n + 1):
            prev[j] = j
        
        # for i in range(w):
        #     dp[i][0] = 0
        
        prev[0]=0
        for i in range(1,w):
            curr=[float('inf')]*(n+1)
            curr[0] = 0
            for j in range(1,n+1):
                
                #nottake = dp[i-1][j]
                nottake = prev[j]

                take=float('inf')
                if nums[i]<=j:
                    #take = 1 + dp[i][j - nums[i]]
                    take=1+curr[j-nums[i]]
                
                curr[j]=min(take,nottake)
            
            prev = curr
        
        return prev[n]
    