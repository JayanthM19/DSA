#https://leetcode.com/problems/triangle/

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        n=len(triangle)
        front=[0]*n
        cur=[0]*n

        for i in range(n):
            front[i]=triangle[n-1][i]
        
        for i in range(n-2,-1,-1):
            cur=[0]*n
            for j in range(i+1):
                cur[j]= triangle[i][j]+min(front[j],front[j+1])
            
            front=cur
        
        return front[0]

        