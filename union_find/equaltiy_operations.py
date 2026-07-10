#https://leetcode.com/problems/satisfiability-of-equality-equations/
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        parent=list(range(26))

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            
            return parent[x]

        def union(a,b):
            pa=find(a)
            pb=find(b)

            if pa!=pb:
                parent[pb]=pa

        for eq in equations:
            if eq[1]=="=":
                union(ord(eq[0])-ord('a'),ord(eq[3])-ord('a'))

        for eq in equations:
            if eq[1]=='!':
                if find(ord(eq[0])-ord('a'))==find(ord(eq[3])-ord('a')):
                    return False
        
        return True

            

