class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if obstacleGrid[0][0]:
            return 0

        m,n=len(obstacleGrid),len(obstacleGrid[0])

        grid=[[0]*n for _ in range(m)]

        grid[0][0]=1
        
        for i in range(1,n):
            if obstacleGrid[0][i]==0:
                grid[0][i]=grid[0][i-1]
            

        for i in range(1,m):
            if obstacleGrid[i][0]==0:
                grid[i][0]=grid[i-1][0]
            
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!=1:
                    grid[i][j]=grid[i-1][j]+grid[i][j-1]
                else:
                    grid[i][j]=0

        return grid[m-1][n-1]