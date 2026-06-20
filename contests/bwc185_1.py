class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """

        
        grid=[["#"]*(n) for _ in range(m)]

        if n<2:
            grid=[["."]*(n) for _ in range(m)]
            
        else:

            grid[0][0]="."
            grid[m-1][n-1]="."
            for i in range(m):
                grid[i][1]="."
    
            for i in range(1,n):
                grid[m-1][i]="."

        
        final=[]
        for i in range(m):
            sub=""
            for j in range(n):
                sub+=grid[i][j]
            final.append(sub)

        return final
                

        