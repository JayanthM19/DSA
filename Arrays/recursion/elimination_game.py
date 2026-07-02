#https://leetcode.com/problems/elimination-game/description/

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        head=1
        remaining=n
        left=True
        steps=1

        while remaining>1:

            if left or remaining%2==1:
                head+=steps
            
            remaining//=2
            steps*=2
            left = not left
        
        return head
