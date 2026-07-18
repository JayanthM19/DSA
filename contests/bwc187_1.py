class Solution(object):
    def rearrangeString(self, s, x, y):
        """
        :type s: str
        :type x: str
        :type y: str
        :rtype: str
        """
        
        t=""
        

        freq=Counter(s)

        num1=freq[y]
        while num1>0:
            t+=y
            num1-=1
    
        for ch,val in freq.items():
            if ch==y:
                continue

            while val>0:
                t+=ch
                val-=1

        return t
            

            
            