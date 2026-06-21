#https://leetcode.com/problems/ones-and-zeroes/


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        #Recursive Solution
        # def count(s):
        #     zeroes,ones=s.count('0'),s.count('1')
        #     return zeroes,ones

        
        # def solve(i,m,n):
        #     if i==len(strs):
        #         return 0
            
        #     zeros, ones = count(strs[i])
            
        #     nottake = solve(i+1,m,n)
        #     take = 0
        #     if zeros <=m and ones<=n:

        #         take=1+solve(i+1,m-zeros,n-ones)
            
        #     return max(take,nottake)

        # return solve(0,m,n)


        #Memoization Method


        # counts=[]
        # for s in strs:
        #     counts.append((s.count('0'),s.count('1')))
        
        # dp={}
        # def solve(i,m,n):
        #     if i==len(strs):
        #         return 0
            
        #     if (i,m,n) in dp:
        #         return dp[(i,m,n)]
            
        #     zeros,ones = counts[i]

        #     nottake = solve(i+1,m,n)
        #     take=0
        #     if zeros<=m and ones<=n:
        #         take=1+solve(i+1,m-zeros,n-ones)
            
        #     dp[(i,m,n)]=max(take,nottake)

        #     return dp[(i,m,n)]

        # return solve(0,m,n)


        #Tabulation Method

        # k=len(strs)

        # counts=[]
        # for s in strs:
        #     counts.append((s.count('0'),s.count('1')))
        
        # dp=[[[0]*(n+1) for _ in range(m+1)]for _ in range(k+1)]

        # for i in range(1,k+1):
        #     zeros,ones=counts[i-1]

        #     for j in range(m+1):
        #         for p in range(n+1):

        #             nottake=dp[i-1][j][p]

        #             take=0

        #             if zeros<=j and ones<=p:
        #                 take = 1+dp[i-1][j-zeros][p-ones]
                    
        #             dp[i][j][p]=max(take,nottake)
        
        # return dp[k][m][n]


        
