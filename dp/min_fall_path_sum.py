#https://leetcode.com/problems/minimum-falling-path-sum/

class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m,n=len(matrix),len(matrix[0])

        front=[0]*n
        for i in range(n):
            front[i]=matrix[m-1][i]
        
        for i in range(m-2,-1,-1):
            cur=[0]*n
            for j in range(n):
                left = front[j-1] if j>0 else float('inf')
                right = front[j+1] if j<n-1 else float('inf')
                cur[j]=matrix[i][j]+min(left,front[j],right)
            
            front = cur
        
        return min(front)
        

