#https://leetcode.com/problems/shift-2d-grid/
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m,c=len(grid),len(grid[0])

        total = m*c

        k%=total

        if not k: return grid

        def shift(i,j):
            while i<j:
                grid[i//c][i%c],grid[j//c][j%c]=grid[j//c][j%c],grid[i//c][i%c]
                i+=1
                j-=1
        shift(0,total-1)
        shift(0,k-1)
        shift(k,total-1)

        return grid


